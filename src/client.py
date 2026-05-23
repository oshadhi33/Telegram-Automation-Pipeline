from telethon import TelegramClient, events
from config import API_ID, API_HASH, PHONE, CHANNEL_USERNAME
from processor import MessageProcessor
from database import Database

class TelegramListener:

    def __init__(self):
        self.client = TelegramClient("session", API_ID, API_HASH)
        self.processor = MessageProcessor()
        self.db = Database()

    async def start(self):
        await self.client.start(PHONE)
        print("Bot started... Listening messages")

        @self.client.on(events.NewMessage(chats=CHANNEL_USERNAME))
        async def handler(event):
            message_data = {
                "id": event.message.id,
                "sender": str(event.sender_id),
                "message": event.raw_text
            }

            processed = self.processor.process(message_data)

            if processed:
                self.db.insert_message(
                    processed["message_id"],
                    processed["sender"],
                    processed["message"]
                )

                print("Stored:", processed)

        await self.client.run_until_disconnected()
