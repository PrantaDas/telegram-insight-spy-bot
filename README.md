# Telegram Insight Spy Bot (SELF BOT)
This project implements a Telegram bot using the Pyrogram library for interacting with the Telegram API. The bot is designed to handle messages in a specific chat, download media files, and store text messages in a CSV file.

## Purpose

The primary purpose of this Telegram bot is to provide a convenient way to manage and store media and text messages from a designated chat. It can be used to automate certain tasks or log interactions within the specified Telegram environment.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- A Telegram account.
- Telegram API credentials (API_ID and API_HASH), which can be obtained by creating a Telegram application at [Telegram Apps](https://my.telegram.org/auth).
- A bot token and a designated chat name for interaction.

## Setup

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/PrantaDas/telegram-insight-spy-bot.git

   cd telegram-insight-spy-bot
   ```
2. **Create a .env file in the project root with the following environment variables:**
    ```sh
    API_ID=your_telegram_api_id
    API_HASH=your_telegram_api_hash
    PHONE_NUMBER=your_phone_number
    PASSWORD=your_telegram_account_password
    BOT_NAME=your_bot_name
    CHAT_NAME=your_designated_chat_name

3. **Install Dependencies:**
    ```sh
    pip install -r requirements.txt

4. **Run the bot:**
    ```sh
    python src/main.py

# Project structure:
* bot.py: Contains the Pyrogram client instance and the message handler.
* utils.py: Utility functions for checking environment variables, creating directories, and writing messages to CSV.
* main.py: Script to run the bot and handle exceptions.

# Usage:
The bot is configured to run with the specified environment variables and handles media and text messages in the designated chat.

# Exception handling:
he main.py script catches specific exceptions related to Pyrogram errors (Unauthorized, BadRequest, Forbidden) and general exceptions.

# Contributing:
Feel free to contribute to the project by opening issues or submitting pull requests.

Made with :heart: by Pranta Das.
