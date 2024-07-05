from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

# Enable info level logging
logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance
chatbot = ChatBot(
    'ExampleBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the English corpus
trainer.train('chatterbot.corpus.english')

# Function to interact with the chatbot
def chat_with_bot():
    print("Type 'exit' to end the conversation.")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            
            bot_response = chatbot.get_response(user_input)
            print(f"Bot: {bot_response}")
        
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

# Start chatting with the bot
chat_with_bot()
