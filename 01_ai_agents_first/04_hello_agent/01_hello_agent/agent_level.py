# Agent Level Custom model configurations

import os
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, function_tool, set_tracing_disabled
from openai import AsyncOpenAI

load_dotenv()

BASE_URL = os.getenv("BASE_URL") or "https://generativelanguage.googleapis.com/v1beta/openai/"
API_KEY = os.getenv("EXAMPLE_API_KEY") or os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME") or "gemini-2.0-flash"

if not BASE_URL or not API_KEY or not MODEL_NAME:
    raise ValueError("Please Set the BASE_URL, API_KEY, and MODEL_NAME environment variables.")

client = AsyncOpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)
set_tracing_disabled(disabled=True)

async def main():
    # This agent will use the custom LLM provider
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client)
    )
    
    result = await Runner.run(agent, "Who is the founder of Pakistan?")
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())