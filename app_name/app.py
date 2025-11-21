# clear; python app_name/app.py

import os

from dotenv import load_dotenv

load_dotenv()  # looks for a .env file in the current directory
print(os.getenv("MY_KEY"))
