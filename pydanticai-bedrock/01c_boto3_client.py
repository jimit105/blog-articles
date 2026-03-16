"""Example 1c: Using a pre-configured boto3 client."""

import boto3

from pydantic_ai import Agent
from pydantic_ai.models.bedrock import BedrockConverseModel
from pydantic_ai.providers.bedrock import BedrockProvider

session = boto3.Session(profile_name="my-profile")
bedrock_client = session.client("bedrock-runtime", region_name="us-east-1")

model = BedrockConverseModel(
    "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    provider=BedrockProvider(bedrock_client=bedrock_client),
)

agent = Agent(model, instructions="You are a helpful assistant.")
result = agent.run_sync("Explain VPCs in one paragraph.")
print(result.output)
