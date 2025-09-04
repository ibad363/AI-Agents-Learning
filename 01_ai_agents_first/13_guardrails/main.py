from agents import (
    Agent, 
    Runner, 
    RunContextWrapper, 
    input_guardrail,
    output_guardrail,
    InputGuardrailTripwireTriggered,
    OutputGuardrailTripwireTriggered,
    GuardrailFunctionOutput, 
    TResponseInputItem
)
from setupconfig import config
import asyncio
from pydantic import BaseModel

# ------------------------example 1---------------------------------


# # Define what our guardrail should output
# class MathHomeworkOutput(BaseModel):
#     is_math_homework: bool
#     reasoning: str

# # Create a simple, fast agent to do the checking
# guardrail_agent = Agent( 
#     name="Homework Police",
#     instructions="Check if the user is asking you to do their math homework.",
#     output_type=MathHomeworkOutput,
# )

# # Create our guardrail function
# @input_guardrail
# async def math_guardrail( 
#     ctx: RunContextWrapper[None], 
#     agent: Agent, 
#     input: str | list[TResponseInputItem]
# ) -> GuardrailFunctionOutput:
#     # Run our checking agent
#     result = await Runner.run(guardrail_agent, input, context=ctx.context, run_config=config)
    
#     # Return the result with tripwire status
#     return GuardrailFunctionOutput(
#         output_info=result.final_output, 
#         tripwire_triggered=result.final_output.is_math_homework,  # Trigger if homework detected
#     )

# # Main agent with guardrail attached
# customer_support_agent = Agent(  
#     name="Customer Support Specialist",
#     instructions="You are a helpful customer support agent for our software company.",
#     input_guardrails=[math_guardrail],  # Attach our guardrail
# )

# # Testing the guardrail
# async def test_homework_detection():
#     try:
#         # This should trigger the guardrail
#         await Runner.run(customer_support_agent, "Can you solve 2x + 3 = 11 for x?", run_config=config)
#         print("❌ Guardrail failed - homework request got through!")
    
#     except InputGuardrailTripwireTriggered:
#         print("✅ Success! Homework request was blocked.")
#         # Handle appropriately - maybe send a polite rejection message

# asyncio.run(test_homework_detection())

# ------------------------example 2---------------------------------

class MessageOutput(BaseModel):
    response: str

class SensitivityCheck(BaseModel):
    contains_sensitive_info: bool
    reasoning: str
    confidence_level: int # 1-10 scale

sensitivity_agent = Agent(
    name="Privacy Guardian",
    instructions="""
    Check if the response contains:
    - Personal information (SSN, addresses, phone numbers)
    - Internal company information
    - Confidential data
    - Inappropriate personal details
    
    Be thorough but not overly sensitive to normal business information.
    """,
    output_type=SensitivityCheck,
)

@output_guardrail
async def privacy_guardrail(
    ctx: RunContextWrapper,
    agent: Agent,
    output: MessageOutput
) -> GuardrailFunctionOutput:
    # Run our sensitivity checking agent
    result = await Runner.run(sensitivity_agent, f"Please analyze this customer service response: {output.response}", context=ctx.context, run_config=config)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.contains_sensitive_info,
    )

# Main customer support agent with output guardrail
support_agent = Agent( 
    name="Customer Support Agent",
    instructions="Help customers with their questions. Be friendly and informative.",
    output_guardrails=[privacy_guardrail],  # Add our privacy check
    output_type=MessageOutput,
)

# Test the output guardrail
async def test_privacy_protection():
    try:
        # This might generate a response with sensitive info
        result = await Runner.run(
            support_agent, 
            "What's my account status for john.doe@email.com?",
            run_config=config
        )
        print(f"✅ Response approved: {result.final_output.response}")
    
    except OutputGuardrailTripwireTriggered as e:
        print("🛑 Response blocked - contained sensitive information!")
        # Send a generic response instead
        fallback_message = "I apologize, but I need to verify your identity before sharing account details."
        print(f"Fallback response: {fallback_message}")

asyncio.run(test_privacy_protection())