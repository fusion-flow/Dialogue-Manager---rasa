import asyncio
from rasa.core.agent import Agent

async def get_bot_response(agent, user_message):
    return await agent.handle_message(user_message)

# Path to your trained Rasa Core model
model_path = "models\core-20240311-155101-achromatic-miso.tar.gz"

# Load the agent with the trained Core model and NLU interpreter
agent = Agent.load(model_path)

user_intent = "greet"

user_message = {
    "text": user_intent,
    "intent": {
        "name": user_intent,
        "confidence": 1.0
        
    },
    "sender_id": "1"
}

print(user_message.sender_id)

# Get response from the agent
# loop = asyncio.get_event_loop()
# response = loop.run_until_complete(get_bot_response(agent, user_message))

response = asyncio.run(agent.handle_message(message=user_message))



# Extract and print the bot's reply
if response:
    bot_reply = response[0]['text']
    print("Bot:", bot_reply) 
else:
    print("No response from the model.")
