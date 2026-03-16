"""Example 5: Prompt Caching — reduce costs with BedrockModelSettings.

NOTE: Bedrock only caches content that exceeds a minimum token threshold
(typically 1024+ tokens for system prompts on Claude). The short system
prompt in this example will likely show 0 for cache write/read tokens.
To see caching in action, use a substantially longer system prompt or
pass a large document as context.
"""

from pydantic_ai import Agent
from pydantic_ai.models.bedrock import BedrockConverseModel, BedrockModelSettings

model = BedrockConverseModel("us.anthropic.claude-sonnet-4-5-20250929-v1:0")

agent = Agent(
    model,
    instructions=(
        "You are a legal document analyst. You have deep expertise in "
        "contract law, intellectual property, and regulatory compliance. "
        "Always cite specific clauses when referencing contract terms. "
        # Imagine this is a much longer system prompt with detailed instructions...
    ),
    model_settings=BedrockModelSettings(
        bedrock_cache_instructions=True,       # Cache the system prompt
        bedrock_cache_tool_definitions=True,   # Cache tool schemas
        bedrock_cache_messages=True,           # Cache the last user message
    ),
)

# First call — cache write (slightly higher cost)
result1 = agent.run_sync("Summarize the key liability clauses in this NDA.")
print(f"Cache write tokens: {result1.usage().cache_write_tokens}")

# Second call — cache read (reduced cost and latency)
result2 = agent.run_sync("What are the termination conditions?")
print(f"Cache read tokens: {result2.usage().cache_read_tokens}")
