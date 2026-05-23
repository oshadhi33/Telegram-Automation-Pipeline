import re
import requests
from config import WEBHOOK_URL

class MessageProcessor:

    def __init__(self):
        self.pattern = re.compile(r".*")

    def is_valid(self, message: str) -> bool:
        return bool(self.pattern.match(message))

    def process(self, message_data):
        message_text = message_data["message"]

        if not self.is_valid(message_text):
            return None

        processed = {
            "message_id": message_data["id"],
            "sender": message_data["sender"],
            "message": message_text
        }

        if WEBHOOK_URL:
            requests.post(WEBHOOK_URL, json=processed)

        return processed
