import asyncio
from src.client import TelegramListener

if __name__ == "__main__":
    listener = TelegramListener()
    asyncio.run(listener.start())
