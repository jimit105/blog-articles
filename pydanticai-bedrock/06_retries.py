"""Example 6: Configuring Retries — adaptive retry with boto3."""

import boto3
from botocore.config import Config
from pydantic_ai import Agent
from pydantic_ai.models.bedrock import BedrockConverseModel
from pydantic_ai.providers.bedrock import BedrockProvider

config = Config(
    retries={
        "max_attempts": 5,
        "mode": "adaptive",  # Handles ThrottlingException with backoff
    }
)

bedrock_client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1",
    config=config,
)

model = BedrockConverseModel(
    "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    provider=BedrockProvider(bedrock_client=bedrock_client),
)

agent = Agent(model, instructions="You are a helpful assistant.")
result = agent.run_sync("What is cloud computing?")
print(result.output)
