# Agent Level Custom model configurations

import os
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from openai import AsyncOpenAI

load_dotenv()

BASE_URL = os.getenv("BASE_URL") or "https://generativelanguage.googleapis.com/v1beta/openai/"
API_KEY = os.getenv("EXAMPLE_API_KEY") or os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME") or "gemini-2.0-flash"

if not BASE_URL or not API_KEY or not MODEL_NAME:
    raise ValueError("Please Set the BASE_URL, API_KEY, and MODEL_NAME environment variables.")

# CLient = Model Provider like OpenAI, Gemini, Claude etc
client = AsyncOpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)
# trace / log workflow of the agent is disabled
set_tracing_disabled(disabled=True)

async def main():
    # This agent will use the custom LLM provider
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client)
    )
    
    # Runner.run for async agent
    result = await Runner.run(agent, "Who is the founder of Pakistan?")
    print(result.final_output) # result is istance of Runner Class bcz it has other properties than final output 
    
if __name__ == "__main__":
    asyncio.run(main())