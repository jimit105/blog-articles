"""Example 1b: Specifying a region or custom credentials."""

from pydantic_ai import Agent
from pydantic_ai.models.bedrock import BedrockConverseModel
from pydantic_ai.providers.bedrock import BedrockProvider

model = BedrockConverseModel(
    "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    provider=BedrockProvider(region_name="us-west-2"),
)

agent = Agent(model, instructions="You are a helpful assistant.")
result = agent.run_sync("Explain VPCs in one paragraph.")
print(result.output)
