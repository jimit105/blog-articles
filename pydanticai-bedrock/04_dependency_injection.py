"""Example 4: Dependency Injection — customer support agent with RunContext."""

from dataclasses import dataclass

from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext


# --- Dependencies ---

@dataclass
class SupportDeps:
    """Dependencies injected into the agent at runtime."""
    customer_id: str
    db: dict  # In production, this would be a database client


# --- Output Schema ---

class SupportResponse(BaseModel):
    answer: str = Field(description="The response to the customer's question")
    order_ids_referenced: list[str] = Field(
        description="Any order IDs mentioned in the response",
        default_factory=list,
    )
    needs_escalation: bool = Field(
        description="Whether this issue needs human escalation",
        default=False,
    )


# --- Agent ---

agent = Agent(
    "bedrock:us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    deps_type=SupportDeps,
    output_type=SupportResponse,
    instructions=(
        "You are a customer support agent. Use the available tools to look up "
        "customer and order information. Be helpful and concise. If you cannot "
        "resolve the issue, set needs_escalation to true."
    ),
)


# --- Tools ---

@agent.tool
async def get_customer_name(ctx: RunContext[SupportDeps]) -> str:
    """Get the current customer's name."""
    customers = ctx.deps.db.get("customers", {})
    return customers.get(ctx.deps.customer_id, {}).get("name", "Unknown")


@agent.tool
async def get_customer_orders(ctx: RunContext[SupportDeps]) -> str:
    """Get the list of orders for the current customer."""
    orders = ctx.deps.db.get("orders", {})
    customer_orders = [
        f"Order {oid}: {o['item']} - {o['status']}"
        for oid, o in orders.items()
        if o["customer_id"] == ctx.deps.customer_id
    ]
    return "\n".join(customer_orders) if customer_orders else "No orders found."


@agent.tool
async def get_order_details(ctx: RunContext[SupportDeps], order_id: str) -> str:
    """Get detailed information about a specific order.

    Args:
        order_id: The order ID to look up.
    """
    orders = ctx.deps.db.get("orders", {})
    order = orders.get(order_id)
    if not order:
        return f"Order {order_id} not found."
    return (
        f"Order {order_id}: {order['item']}, "
        f"Status: {order['status']}, "
        f"Placed: {order['date']}, "
        f"Total: ${order['total']:.2f}"
    )


# --- Run ---

# Simulated database
fake_db = {
    "customers": {
        "C-1001": {"name": "Alice Johnson", "email": "[email]"},
    },
    "orders": {
        "ORD-5001": {
            "customer_id": "C-1001",
            "item": "Wireless Headphones",
            "status": "Delivered",
            "date": "2026-02-15",
            "total": 79.99,
        },
        "ORD-5002": {
            "customer_id": "C-1001",
            "item": "USB-C Hub",
            "status": "In Transit",
            "date": "2026-03-10",
            "total": 45.00,
        },
    },
}

deps = SupportDeps(customer_id="C-1001", db=fake_db)
result = agent.run_sync("Where is my latest order?", deps=deps)

response: SupportResponse = result.output
print(f"Answer: {response.answer}")
print(f"Orders referenced: {response.order_ids_referenced}")
print(f"Needs escalation: {response.needs_escalation}")
