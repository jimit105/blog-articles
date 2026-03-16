"""Example 7: Bedrock Guardrails — content filtering via BedrockModelSettings.

BEFORE RUNNING: Replace 'your-guardrail-id' with an actual guardrail ID
from your AWS account. Create one in the Bedrock console under
Guardrails → Create guardrail. The identifier will look something
like 'abc123def456'.
"""

from pydantic_ai import Agent
from pydantic_ai.models.bedrock import BedrockConverseModel, BedrockModelSettings

model = BedrockConverseModel("us.anthropic.claude-sonnet-4-5-20250929-v1:0")

agent = Agent(
    model,
    instructions="You are a customer-facing assistant.",
    model_settings=BedrockModelSettings(
        bedrock_guardrail_config={
            "guardrailIdentifier": "your-guardrail-id",  # Replace with your guardrail ID from the Bedrock console
            "guardrailVersion": "1",
            "trace": "enabled",
        }
    ),
)

result = agent.run_sync("Tell me about your return policy.")
print(result.output)
