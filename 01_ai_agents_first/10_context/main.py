import os
from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel, Runner, RunConfig, handoff, RunContextWrapper, function_tool
from openai import AsyncOpenAI
import asyncio
from dataclasses import dataclass

# Load the environment variables from the .env file
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

gemini_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=gemini_client
)

config = RunConfig(
    model=gemini_model,
    model_provider=gemini_client, # type: ignore
    tracing_disabled=True
)

# define a simple context using a dataclass
@dataclass
class UserInfo:
    name: str
    uid: int

# A tool function that access local context via wrapper
@function_tool
async def fetch_user (wrapper: RunContextWrapper[UserInfo]) -> str:
    return f"User {wrapper.context.name} is 22 years old"

async def main():
    # create a context object
    user_info = UserInfo("Ibad", 1)
    
    # Define an agent that will use the tool above
    agent = Agent(
        name="Assistant",
        # instructions="give assistant in 1 line.",
        tools=[fetch_user]
    )
    
    # run the agent, passing local context
    result = await Runner.run(
        starting_agent=agent,
        input="What is the name of the user?",
        run_config=config,
        context=user_info
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())