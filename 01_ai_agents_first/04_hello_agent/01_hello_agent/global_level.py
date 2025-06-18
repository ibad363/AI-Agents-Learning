# Set Model(LLM) configration on Global level

import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import (
    Agent, 
    Runner, 
    function_tool,
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled
)

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

set_default_openai_client(client, use_for_tracing=False)
set_default_openai_api("chat_completions")
set_tracing_disabled(disabled=True)

@function_tool
def get_weather(city: str):
    print(f"[debug] getting weather for {city}")
    return f"The weather in {city} is sunny."

async def main():
    agent = Agent(
        name="Assistant",
        # instructions="You only respond in haikus.",
        instructions="You respond the weather.",
        model=MODEL_NAME,
        tools=[get_weather]
    )
    
    result = await Runner.run(agent, "What's the weather in Tokyo?")
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())