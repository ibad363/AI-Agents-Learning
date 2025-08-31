from agents import Agent, Runner, ModelSettings, function_tool
from setupconfig import config
from pretty_print import print_pretty_json

# Base agent
base_agent = Agent(
    name="BaseAssistant",
    instructions="You are a helpful assistant.",
    model_settings=ModelSettings(temperature=0.7)
)

# Simple clone
friendly_agent = base_agent.clone(
    name="FriendlyAssistant",
    instructions="You are a very friendly and warm assistant."
)

# Test both agents
query = "Hello, how are you?"

# result_base = Runner.run_sync(base_agent, query, run_config=config)
# result_friendly = Runner.run_sync(friendly_agent, query, run_config=config)

# print("Base Agent:", result_base.final_output)
# print("Friendly Agent:", result_friendly.final_output)

# Clone with different temperature
creative_agent = base_agent.clone(
    name="CreativeAssistant",
    instructions="You are a creative writing assistant.",
    model_settings=ModelSettings(temperature=0.9)  # Higher creativity
)

precise_agent = base_agent.clone(
    name="PreciseAssistant", 
    instructions="You are a precise, factual assistant.",
    model_settings=ModelSettings(temperature=0.1)  # Lower creativity
)

# Test creativity levels
query = "Describe a sunset."

# result_creative = Runner.run_sync(creative_agent, query, run_config=config)
# result_precise = Runner.run_sync(precise_agent, query, run_config=config)

# print("Creative:", result_creative.final_output)
# print("Precise:", result_precise.final_output)


@function_tool
def calculate_area(length: float, width: float) -> str:
    return f"Area = {length * width} square units"

@function_tool
def get_weather(city: str) -> str:
    return f"Weather in {city}: Sunny, 72°F"

# Base agent with one tool
base_agent = Agent(
    name="BaseAssistant",
    tools=[calculate_area],
    instructions="You are a helpful assistant."
)

# Clone with additional tool
weather_agent = base_agent.clone(
    name="WeatherAssistant",
    tools=[calculate_area, get_weather],  # New tools list
    instructions="You are a weather and math assistant."
)

# Clone with different tools
math_agent = base_agent.clone(
    tools=[calculate_area],  # Same tools
    instructions="You are a math specialist."
)

# base_agent.tools.append(calculate_area)
# print("-" * 50)
# print("base_agent.tools")
# print_pretty_json(base_agent.tools)

# print("-" * 50)
# print("weather_agent.tools")
# print_pretty_json(weather_agent.tools)

# print("-" * 50)
# print("math_agent.name")
# print_pretty_json(math_agent.name)

# print("-" * 50)
# print("math_agent.tools")
# print_pretty_json(math_agent.tools)

# 🎭 Advanced Examples

# Create a base agent
base_agent = Agent(
    name="BaseAssistant",
    instructions="You are a helpful assistant.",
    model_settings=ModelSettings(temperature=0.7)
)

# Create multiple specialized variants
agents = {
    "Creative": base_agent.clone(
        name="CreativeWriter",
        instructions="You are a creative writer. Use vivid language.",
        model_settings=ModelSettings(temperature=0.9)
    ),
    "Precise": base_agent.clone(
        name="PreciseAssistant", 
        instructions="You are a precise assistant. Be accurate and concise.",
        model_settings=ModelSettings(temperature=0.1)
    ),
    "Friendly": base_agent.clone(
        name="FriendlyAssistant",
        instructions="You are a very friendly assistant. Be warm and encouraging."
    ),
    "Professional": base_agent.clone(
        name="ProfessionalAssistant",
        instructions="You are a professional assistant. Be formal and business-like."
    )
}

# Test all variants
query = "Tell me about artificial intelligence."

# for name, agent in agents.items():
#     result = Runner.run_sync(agent, query, run_config=config)
#     print(f"\n{name} Agent:")
#     print(result.final_output[:100] + "...")

# 5. Understanding Shared References

# Demonstrate shared references
original_agent = Agent(
    name="Original",
    tools=[calculate_area],
    instructions="You are helpful."
)

# Clone without new tools list
shared_clone = original_agent.clone(
    name="SharedClone",
    instructions="You are creative."
)

# Add tool to original
@function_tool
def new_tool() -> str:
    return "I'm a new tool!"

original_agent.tools.append(new_tool)

# Check if clone also has the new tool
# print("Original tools:", len(original_agent.tools))  # 2
# print("Clone tools:", len(shared_clone.tools))      # 2 (shared!)

# Create independent clone
independent_clone = original_agent.clone(
    name="IndependentClone",
    tools=[calculate_area],  # New list
    instructions="You are independent."
)

original_agent.tools.append(new_tool)
# print("Independent clone tools:", len(independent_clone.tools))  # 1 (independent!)
# print("original_agent tools:", len(original_agent.tools))  # 1 (independent!)


# Exercise 1: Create Agent Variants
# Create a base agent
base_agent = Agent(
    name="BaseAssistant",
    instructions="You are a helpful assistant.",
    model_settings=ModelSettings(temperature=0.7)
)

# Create 3 different variants
variants = {
    "Poet": base_agent.clone(
        name="Poet",
        instructions="You are a poet. Respond in verse.",
        model_settings=ModelSettings(temperature=0.9)
    ),
    "Scientist": base_agent.clone(
        name="Scientist", 
        model_settings=ModelSettings(temperature=0.1)
    ),
    "Chef": base_agent.clone(
        instructions="You are a chef. Talk about food and cooking."
    )
}

# Test all variants
query = "What is love?"

for name, agent in variants.items():
    result = Runner.run_sync(agent, query, run_config=config)
    print(f"\n{name}:")
    print(result.final_output)