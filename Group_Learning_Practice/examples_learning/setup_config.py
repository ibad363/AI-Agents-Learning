import os
from dotenv import load_dotenv
from agents import OpenAIChatCompletionsModel, RunConfig
from openai import AsyncOpenAI

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