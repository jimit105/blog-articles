"""Example 2: Structured Output — validated Pydantic model as output."""

from pydantic import BaseModel, Field
from pydantic_ai import Agent


class MovieReview(BaseModel):
    title: str = Field(description="The movie title")
    rating: float = Field(description="Rating from 0.0 to 10.0", ge=0, le=10)
    pros: list[str] = Field(description="List of positive aspects")
    cons: list[str] = Field(description="List of negative aspects")
    summary: str = Field(description="One-sentence summary of the review")


agent = Agent(
    "bedrock:us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    output_type=MovieReview,
    instructions="You are a movie critic. Analyze the given movie and provide a structured review.",
)

result = agent.run_sync("Review the movie 'Interstellar'")
review: MovieReview = result.output

print(f"Title: {review.title}")
print(f"Rating: {review.rating}/10")
print(f"Pros: {', '.join(review.pros)}")
print(f"Cons: {', '.join(review.cons)}")
print(f"Summary: {review.summary}")
