# Run Level Custom model configurations

import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import (
    Agent, 
    Runner,
    OpenAIChatCompletionsModel,
)
from agents.run import RunConfig

load_dotenv()

API_KEY = os.getenv("EXAMPLE_API_KEY") or os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Please Set the API_KEY environment variables.")

client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client, # type: ignore
    tracing_disabled=True
)
def main():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
    )
    
    result = Runner.run_sync(agent, "What's the simplest library for scrolling animation for next js?, answer in 3 lines", run_config=config)
    print(result.final_output)
    
if __name__ == "__main__":
    main()