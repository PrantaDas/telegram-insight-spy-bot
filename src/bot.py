"""
Telegram Bot Script

This script initializes a Pyrogram client, sets up necessary environment variables,
and defines a message handler to process messages in a specified chat.

Dependencies:
- Python 3.x
- Pyrogram library
- dotenv library

Usage:
1. Set up a .env file with the required environment variables:
   - API_ID
   - API_HASH
   - PHONE_NUMBER
   - PASSWORD
   - BOT_NAME
   - CHAT_NAME

2. Run the script.

Note: Ensure that the 'utils' module is available and contains the required functions.

"""

from dotenv import load_dotenv
import os
from pyrogram import Client, filters

# Internal
from utils import check_envs_and_values, write_message_to_csv, get_media


load_dotenv()

# List of required env variables
env_vars = ['API_ID','API_HASH','PHONE_NUMBER','PASSWORD','BOT_NAME','CHAT_NAME']

# Check that every env vars are set
check_envs_and_values(env_vars)

# Retrieve the env varsff
BOT_NAME = os.environ.get('BOT_NAME')
API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
PASSWORD = os.environ.get('PASSWORD')
PHONE_NUMBER = os.environ.get('PHONE_NUMBER')
CHAT_NAME = os.environ.get('CHAT_NAME')

#  Initialize Pyrogram client
app = Client (
    BOT_NAME,
    api_id = API_ID,
    api_hash = API_HASH,
    phone_number = PHONE_NUMBER,
    password = PASSWORD
    )

@app.on_message(filters.private  | filters.channel)
async def get_messages(client, message):
    """
    Message handler function that processes messages in a specified chat.
    Downloads media files and writes text messages to a CSV file.

    Parameters:
    - client: The Pyrogram client instance.
    - message: The Telegram message to be processed.

    Returns:
    - None
    """
    if message.chat and message.chat.title == CHAT_NAME:
        if  message.media:
            await get_media(message, app)
        
        else:
            write_message_to_csv(message)
        
    else:
        return