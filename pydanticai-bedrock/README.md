# PydanticAI + Amazon Bedrock Examples

Code examples from the blog post: [Building AI Agents with PydanticAI and Amazon Bedrock](https://jimit105.substack.com/)

## Prerequisites

- Python 3.10+
- AWS account with [Bedrock model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) enabled
- AWS credentials configured (`~/.aws/credentials`, environment variables, or IAM role)

## Setup

```bash
pip install -r requirements.txt
```

## Examples

| File | Description |
|---|---|
| `01_simple_agent.py` | Basic agent with Bedrock |
| `02_structured_output.py` | Validated Pydantic model as output |
| `03_tool_calling.py` | Agent with a weather lookup tool |
| `04_dependency_injection.py` | Dependency injection with RunContext |
| `05_prompt_caching.py` | Cost optimization with prompt caching |
| `06_retries.py` | Adaptive retry configuration |
| `07_guardrails.py` | Bedrock Guardrails for content filtering |
| `08_async_usage.py` | Production async pattern |
| `09_token_usage.py` | Token usage tracking |

## Running

```bash
python 01_simple_agent.py
```

> **Note:** `07_guardrails.py` requires a guardrail created in the Bedrock console. See the file comments for setup instructions.

## Blog Post

Read the full walkthrough: [Building AI Agents with PydanticAI and Amazon Bedrock](https://jimit105.substack.com/)
