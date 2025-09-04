from setupconfig import config
from agents import Agent, Runner, SQLiteSession
import asyncio

# --------------------- Example 1 --------------------------

# # Create session memory
# session = SQLiteSession("my_first_conversation")

# # Create agent
# agent = Agent(
#     name="Assistant",
#     instructions="You are a helpful assistant. Be friendly and remember our conversation.",
# )

# print("=== First Conversation with Memory ===")

# # Turn 1
# result1 = Runner.run_sync(
#     agent,
#     "Hi! My name is Alex and I love pizza.",
#     session=session,
#     run_config=config
# )
# print("Agent:", result1.final_output)

# # Turn 2 - Agent should remember your name!
# result2 = Runner.run_sync(
#     agent,
#     "What's my name?",
#     session=session,
#     run_config=config
# )
# print("Agent:", result2.final_output)  # Should say "Alex"!

# # Turn 3 - Agent should remember you love pizza!
# result3 = Runner.run_sync(
#     agent,
#     "What food do I like?",
#     session=session,
#     run_config=config
# )
# print("Agent:", result3.final_output)  # Should mention pizza!

# --------------------- Example 2 --------------------------

# # Temporary memory (lost when program ends)
# temp_session = SQLiteSession("temp_conversation")

# # Persistent memory (saved to file)
# persistent_session = SQLiteSession("user_123", "conversations.db")

# agent = Agent(name="Assistant", instructions="You are helpful.")

# # Use temporary session
# # Turn 1 - set favorite color
# result1 = Runner.run_sync(
#     agent,
#     "Remember: my favorite color is blue",
#     session=temp_session,
#     run_config=config
# )
# print("Agent (temp session):", result1.final_output)

# # Turn 2 - should remember in this session
# result1 = Runner.run_sync(
#     agent,
#     "What's my favorite color?",
#     session=temp_session,
#     run_config=config
# )
# print("Agent (temp session):", result1.final_output)  # Should say "blue"!

# # Use persistent session
# # Turn 1 - set favorite color
# result2 = Runner.run_sync(
#     agent,
#     "Remember: my favorite color is blue",
#     session=persistent_session,
#     run_config=config
# )
# print("Agent (persistent session):", result2.final_output)

# # Turn 2 - should remember in this session
# result2 = Runner.run_sync(
#     agent,
#     "What's my favorite color?",
#     session=persistent_session,
#     run_config=config
# )
# print("Agent (persistent session):", result2.final_output)  # Should say "blue"!

# print("Both sessions now remember your favorite color!")
# print("But only the persistent session will remember after restarting the program.")



# --------------------- Example 3 --------------------------
# ----3. Memory Operations - Adding, Viewing, and Removing----


# async def memory_operations_demo():
#     session = SQLiteSession("memory_ops", "test.db")

#     # Add some conversation items manually
#     conversation_items = [
#         {"role": "user", "content": "Hello!"},
#         {"role": "assistant", "content": "Hi there! How can I help you?"},
#         {"role": "user", "content": "What's the weather like?"},
#         {"role": "assistant", "content": "I don't have access to weather data."}
#     ]

#     await session.add_items(conversation_items)
#     print("Added conversation to memory!")

#     # View all items in memory
#     items = await session.get_items()
#     print(f"\nMemory contains {len(items)} items:")
#     for item in items:
#         print(f"  {item['role']}: {item['content']}")

#     # Remove the last item (undo)
#     last_item = await session.pop_item()
#     print(f"\nRemoved last item: {last_item}")

#     # View memory again
#     items = await session.get_items()
#     print(f"\nMemory now contains {len(items)} items:")
#     for item in items:
#         print(f"  {item['role']}: {item['content']}")

#     # Clear all memory
#     await session.clear_session()
#     print("\nCleared all memory!")

#     # Verify memory is empty
#     items = await session.get_items()
#     print(f"Memory now contains {len(items)} items")

# # Run the async demo
# asyncio.run(memory_operations_demo())




# --------------------- Example 4 --------------------------
# 🏗️ Real-World Applications
# Self Challenge Project Customer Support ChatAgent


# class CustomerSupportBot:
#     def __init__(self):
#         self.agent = Agent(
#             name="SupportBot",
#             instructions="""You are a helpful customer support agent.
#             Remember the customer's information and previous issues throughout the conversation.
#             Be friendly and professional."""
#         )

#     def get_customer_session(self, customer_id: str):
#         """Get or create a session for a specific customer"""
#         return SQLiteSession(f"customer_{customer_id}", "support_conversations.db")

#     def chat_with_customer(self, customer_id: str, message: str):
#         """Handle a customer message"""
#         session = self.get_customer_session(customer_id)

#         result = Runner.run_sync(
#             self.agent,
#             message,
#             session=session,
#             run_config=config
#         )

#         return result.final_output

# # Example usage
# support_bot = CustomerSupportBot()

# # Customer 123's conversation
# print("=== Customer 123 Support Session ===")
# print("Customer: Hi, I'm having trouble with my order #12345")
# response1 = support_bot.chat_with_customer("123", "Hi, I'm having trouble with my order #12345")
# print(f"Support: {response1}")

# print("\nCustomer: The item was damaged when it arrived")
# response2 = support_bot.chat_with_customer("123", "The item was damaged when it arrived")
# print(f"Support: {response2}")

# print("\nCustomer: What was my order number again?")
# response3 = support_bot.chat_with_customer("123", "What was my order number again?")
# print(f"Support: {response3}")  # Should remember order #12345!

# # Different customer's conversation
# print("\n=== Customer 456 Support Session ===")
# print("Customer: Hello, I need help with billing")
# response4 = support_bot.chat_with_customer("456", "Hello, I need help with billing")
# print(f"Support: {response4}")  # Fresh conversation, no memory of customer 123


# --------------------- Key Points --------------------------

# Memory persistence

# Use in-memory SQLite (SQLiteSession("session_id")) for temporary conversations

# Use file-based SQLite (SQLiteSession("session_id", "path/to/db.sqlite")) for persistent conversations

# Use SQLAlchemy-powered sessions (SQLAlchemySession("session_id", engine=engine, create_tables=True)) for production systems with existing databases supported by SQLAlchemy

# Use OpenAI-hosted storage (OpenAIConversationsSession()) when you prefer to store history in the OpenAI Conversations API

# Consider implementing custom session backends for other production systems (Redis, Django, etc.) for more advanced use cases