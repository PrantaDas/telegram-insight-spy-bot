from typing import List
import os
import csv
from pyrogram.errors import ChatWriteForbidden, PeerIdInvalid
from pyrogram import types


def check_envs_and_values(env_var_names: List[str]) -> None:
    """
    Checks if the specified environment variables are present and have non-empty values.

    Parameters:
    - env_var_names (List[str]): A list of environment variable names to be checked.

    Raises:
    - ValueError: If any of the specified environment variables is missing or has an empty value.

    Returns:
    - None: If all specified environment variables are present and have non-empty values.

    Example:
    >>> check_envs_and_values(['DATABASE_URL', 'SECRET_KEY'])
    => All the env vars are loaded
    """
    missing_vars = [env_var for env_var in env_var_names if env_var not in os.environ]
    empty_vars = [env_var for env_var in env_var_names if not os.environ.get(env_var)]

    if missing_vars:
        raise ValueError(f"Missing environment variable(s): {', '.join(missing_vars)}")

    if empty_vars:
        raise ValueError(f"Empty values for environment variable(s): {', '.join(empty_vars)}")

    print('=> All the env vars are loaded')



def create_dir(csv_folder : str, files_folder :str) -> None:
    """
    Creates directories if they do not exist.

    Parameters:
    - csv_folder (str): Path to the CSV folder to be created.
    - files_folder (str): Path to the files folder to be created.

    Raises:
    - IOError: If an unexpected error occurs while creating directories.

    Returns:
    - None: If directories are created successfully or already exist.

    Example:
    >>> create_dir('data/csv', 'data/files')
    """
    try:
        if csv_folder and not os.path.exists(csv_folder):
            os.makedirs(csv_folder)
    
        if files_folder and not os.path.exists(files_folder):
            os.makedirs(files_folder)

    except IOError as e:
        raise IOError(f"Unexpected error occured while creating directory error: {str(e)}")


def write_message_to_csv(message: dict, file_name: str = 'message.csv'):
    """
    Writes a message to a CSV file, creating the file and necessary directory structure if needed.

    Parameters:
    - message (dict): The message information to be written to the CSV file.
    - file_name (str): The name of the CSV file to write the message to (default is 'message.csv').

    Raises:
    - IOError: If an error occurs while creating directories or writing to the CSV file.
    - ValueError: If the 'file_name' parameter is not a string.

    Returns:
    - None: If the message is successfully written to the CSV file.

    Example:
    >>> write_message_to_csv({'id': 123, 'date': '2024-01-05', 'author_signature': 'John Doe', 'text': 'Hello World!'})
    """
    try:
        create_dir('csvs', None)
        
        if not isinstance(file_name, str):
            raise ValueError("The 'file_name' parameter must be a string.")
        
        file_path = os.path.join(os.curdir, 'csvs', file_name)

        if not os.path.isfile(file_path):
            with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
                headers = ['Message Id', 'Date', 'From User', 'Text']
                writer = csv.writer(csv_file)
                writer.writerow(headers)
        
        with open(file_path, 'a', newline='', encoding='utf8') as file:
            writer = csv.writer(file)
            writer.writerow ([message.id,message.date,getattr(message,'author_signature','N/A'),message.text or 'N/A'])

    except IOError as e:
        raise IOError(f"Error writing to CSV file: {str(e)}")
    

async def get_media(message:types.Message, app) -> None:
    """
    Downloads media from a Telegram message and saves it to the 'files' directory.

    Parameters:
    - message (types.Message): The Telegram message containing media to be downloaded.
    - app: The Telegram client application.

    Raises:
    - IOError: If an error occurs while downloading or saving the media file.
    - ChatWriteForbidden: If the bot does not have permission to write in the chat.
    - PeerIdInvalid: If the provided peer ID is invalid.

    Returns:
    - None: If the media file is successfully downloaded and saved.

    Example:
    >>> await get_media(message, telegram_app)
    """
    try:
        create_dir(None,'files')
        file_path = os.path.join(os.getcwd(),'files')
        await app.download_media(message,file_path+'/')
    
    except (IOError, ChatWriteForbidden, PeerIdInvalid) as e:
        raise IOError(f"Error downloading or saving file: {str(e)}")

