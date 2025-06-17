from dotenv import load_dotenv
import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig
from openai import AsyncOpenAI

load_dotenv()
openrouter_api_key = os.getenv("OPEN_ROUTER_API_KEY")

if not openrouter_api_key:
    raise Exception("OPEN_ROUTER_API_KEY is not set")

# setup openrouter client like openAI but via open router
external_client = AsyncOpenAI(
    api_key= openrouter_api_key,
    base_url= "https://openrouter.ai/api/v1"
)

# choose any openrouter supported model
model = OpenAIChatCompletionsModel(
    model="qwen/qwen3-30b-a3b:free",
    openai_client=external_client
)

# setup config
config = RunConfig(
    model=model,
    model_provider=external_client, # type: ignore
    tracing_disabled=True
)

# define agent
agent = Agent(
    name="Translator",
    instructions="you are a helpful translator, always translate from english to urdu",
)

# input and run agent
response = Runner.run_sync(
    agent, 
    input="my name is Ibad ur Rehman and I am from Pakistan and I am 22 years old and i am agentic ai developer",
    run_config = config
)

# output
print(response.final_output)