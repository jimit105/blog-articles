"""Example 8: Async Usage — production-recommended async pattern."""

import asyncio
from pydantic_ai import Agent

agent = Agent("bedrock:us.anthropic.claude-sonnet-4-5-20250929-v1:0")


async def main():
    result = await agent.run("Explain async/await in Python.")
    print(result.output)


asyncio.run(main())
