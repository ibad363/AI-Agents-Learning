from agents import function_tool,Runner, Agent, ModelSettings, enable_verbose_stdout_logging
from setupconfig import config

# enable_verbose_stdout_logging()
@function_tool
def calculate_area(length: float, width: float) -> str:
    """Calculate the area of a rectangle."""
    import time
    time.sleep(1)
    area = length * width
    return f"Area = {length} × {width} = {area} square units"

# Agent that MUST use tools
tool_user = Agent(
    name="Tool User",
    instructions="You are a helpful assistant. Always use tools when available.",
    tools=[calculate_area],
    model_settings=ModelSettings(tool_choice="required"),
    # reset_tool_choice=False
)

result = Runner.run_sync(tool_user, "What's the capital of America?",run_config=config)
print(result.final_output)