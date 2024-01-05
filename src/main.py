"""
Bot Runner Script

This script runs the Pyrogram bot instance and handles potential exceptions.

Dependencies:
- Python 3.x
- Pyrogram library

Usage:
1. Ensure the 'bot' module is available and contains the Pyrogram app instance.
2. Run the script.

Note: The script catches specific exceptions related to Pyrogram errors and general exceptions.

"""

from pyrogram.errors import Forbidden, BadRequest, Unauthorized

# Internal
from bot import app

if __name__ == '__main__':
    try:
        print('=> Bot started')
        app.run()

    except Unauthorized as e:
        print(e)
    
    except BadRequest as e:
        print(e)

    except Forbidden as e:
        print(e)

    except KeyboardInterrupt as e:
        print(f"KeyboardInterrupt: {e}")
    
    except Exception as e:
        print(f"Exception: {e}")