"""Example 9: Token Usage Tracking — monitor costs per request."""

from pydantic_ai import Agent

agent = Agent(
    "bedrock:us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    instructions="You are a helpful assistant. Be concise.",
)

result = agent.run_sync("Hello!")
usage = result.usage()
print(f"Request tokens: {usage.request_tokens}")
print(f"Response tokens: {usage.response_tokens}")
print(f"Total tokens: {usage.total_tokens}")
