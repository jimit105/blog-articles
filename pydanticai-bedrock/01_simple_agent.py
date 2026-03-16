"""Example 1: A Simple Agent — basic Bedrock usage."""

from pydantic_ai import Agent

agent = Agent(
    "bedrock:us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    instructions="You are a helpful assistant. Be concise.",
)

result = agent.run_sync("What are the three laws of thermodynamics?")
print(result.output)
