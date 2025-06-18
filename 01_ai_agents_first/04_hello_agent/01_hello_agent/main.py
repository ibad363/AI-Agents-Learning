from agents import Agent, Runner, OpenAIChatCompletionsModel, function_tool
from agents.run import RunConfig
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio

# Run Google Gemini with OPENAI-Agent SDK
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")


external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client, # type: ignore
    tracing_disabled=True
)

# Hello world code | method one
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model=model,
)

# result = Runner.run_sync(agent, "Write a haiku about recursion in programming.", run_config=config)

# print("Calling Agent")
# print(result.final_output)


# Hello world code | method two
async def main():
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
    )

    result = await Runner.run(agent, "Tell me about recursion in programming.",run_config=config)
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())

# Run with OpenAI API
# from agents import Agent, Runner

# agent = Agent(name=None, instructions=None, model='gpt-4.1-mini') # type: ignore

# result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
# print(result.final_output)