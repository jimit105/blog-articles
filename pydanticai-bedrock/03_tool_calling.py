"""Example 3: Tool Calling — agent with a weather lookup tool."""

import httpx
from pydantic_ai import Agent


agent = Agent(
    "bedrock:us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    instructions=(
        "You are a weather assistant. Use the get_weather tool to look up "
        "current weather conditions, then provide a helpful summary."
    ),
)


@agent.tool_plain
async def get_weather(city: str) -> str:
    """Get the current weather for a city.

    Args:
        city: The city name to look up weather for.
    """
    # Using a free weather API (no key required)
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://wttr.in/{city}",
            params={"format": "j1"},
        )
        data = response.json()
        current = data["current_condition"][0]
        return (
            f"Temperature: {current['temp_C']}°C, "
            f"Feels like: {current['FeelsLikeC']}°C, "
            f"Condition: {current['weatherDesc'][0]['value']}, "
            f"Humidity: {current['humidity']}%"
        )


result = agent.run_sync("What's the weather like in Seattle right now?")
print(result.output)
