from agents import Agent, Runner, ModelSettings, function_tool
from setupconfig import config

# Base agent
base_agent = Agent(
    name="BaseAssistant",
    instructions="You are a helpful assistant.",
    model_settings=ModelSettings(temperature=0.7)
)

# Clone with different instructions
creative_agent = base_agent.clone(
    instructions="You are a creative writing assistant."
)
print(creative_agent)