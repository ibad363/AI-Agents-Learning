import os
from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel, Runner, RunConfig, handoff, RunContextWrapper
from openai import AsyncOpenAI
import asyncio

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

# Agent specializing in refund processes
refund_agent = Agent(
    name="Refund Agent",
    instructions="You handle all refund related processes. Assist users in processing refunds efficiently."
)

# Agent specializing in billing inquiries
billing_agent = Agent(
    name="Billing Agent",
    instructions="You handle all billing-related inquiries. Provide clear and concise information regarding billing issues."
)

# Triage agent that decides which specialist agent to hand off tasks to
triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which specialist agent handle user requests based on the nature of the inquiry.",
    handoffs=[refund_agent, billing_agent]
)

user_input = "I need a refund for my recent purchase."

# result = Runner.run_sync(
#     starting_agent=triage_agent,
#     input=user_input,
#     run_config=config,
# )

# print(result.final_output)


# Customizing handoffs via the handoff() function

urdu_agent = Agent(
    name="Urdu Agent",
    instructions="You only speak Urdu.",
)

english_agent = Agent(
    name="English Agent",
    instructions="You only speak English.",
)

def on_handoff(agent: Agent, ctx: RunContextWrapper):
    agent_name = agent.name
    print(f"Handoff: Agent {agent_name} is handling the task.")
    print(f"Input: {ctx.context}")

urdu_agent_handoff = handoff(
    agent=urdu_agent,
    on_handoff= lambda ctx:on_handoff(urdu_agent, ctx),
)

english_agent_handoff = handoff(
    agent=english_agent,
    on_handoff= lambda ctx:on_handoff(english_agent, ctx),
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which specialist agent handle user requests based on the nature of the inquiry.",
    handoffs=[urdu_agent_handoff, english_agent_handoff]
)

# Run the triage agent with custom handoffs
async def main(input: str):
    result = await Runner.run(
        starting_agent=triage_agent,
        input=input,
        run_config=config,
    )

    print(result.final_output)
    
# asyncio.run(main("Hi! How are you?"))
asyncio.run(main("السلام عليكم"))