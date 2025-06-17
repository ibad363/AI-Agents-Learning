import os
from dotenv import load_dotenv
import chainlit as cl
from litellm import completion
import json

# Load environment variables from .env file
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

@cl.on_chat_start
async def start():
    """Set up the chat session when a user connects."""
    # Initialize an empty chat history in the session.
    cl.user_session.set("chat_history", [])
    
    await cl.Message(content="Welcome to Ibad Assistant").send()
    
    
@cl.on_message
async def main(message: cl.Message):
    """Process the user's message and generate a response."""
    # send a thinking message
    msg = cl.Message(content="Thinking...")
    await msg.send()
    
    # Retrieve the chat history from the session.
    history = cl.user_session.get("chat_history") or []
    
    # append the user's message to the chat history
    history.append({"role": "user", "content": message.content})
    
    try:
        # get completion from LiteLLM
        response = completion(
            model= "gemini/gemini-2.0-flash",
            api_key=gemini_api_key,
            messages=history
        )
        
        response_content = response.choices[0].message.content # type: ignore
        
        msg.content = response_content # type: ignore
        await msg.update()
        
        # append the assistant's message to the chat history
        history.append({"role": "assistant", "content": response_content})
        
        # update the chat history in the session
        cl.user_session.set("chat_history", history)
        
        # optional: log the interaction
        # print("User: ", message.content)
        # print("Assistant: ", response_content)
        
    except Exception as e:
        msg.content = f"Error: {e}"
        await msg.update()
        print(f"Error: {e}")
        

@cl.on_chat_end
async def on_chat_end():
    # retreive the full chat history at the end of session
    history = cl.user_session.get("chat_history") or []
    # save the chat history to a file
    with open("chat_history.json", "w") as f:
        json.dump(history, f, indent=2)
    print("Chat history saved to chat_history.json")