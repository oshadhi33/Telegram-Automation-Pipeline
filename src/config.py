import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
PHONE = os.getenv("PHONE")

CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", None)

DB_NAME = "messages.db"
