from telegram import Bot

# Replace 'your_bot_token' with your actual bot token
bot = Bot(token='6850222824:AAFdcopdWuSZpTgl65bUwDOTqtnO4MrIeek')

# Get the chat ID of the user
user_chat_id = bot.get_updates()[-1].message.chat_id

print(f'User Chat ID: {user_chat_id}')
