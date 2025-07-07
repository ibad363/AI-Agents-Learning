import chainlit as cl

@cl.on_chat_start
async def start():
    """Set up the chat session when a user connects."""
    
    # Initialize an empty chat history in the session.
    cl.user_session.set("chat_history", [])
    
    await cl.Message(content="Welcome to Ibad Assistant.").send()

@cl.on_message
async def main(message: cl.Message):    
    await cl.Message(
            content=f"Received: {message.content}",
        ).send()