# Telegram Automation Pipeline

## Overview
This project demonstrates a real-time Telegram automation pipeline using Telethon. It listens to messages from a Telegram channel, processes them, stores them in a database, and optionally sends webhook notifications.

## Features
- Real-time Telegram message listening
- Message filtering using regex
- SQLite database storage
- Webhook integration (n8n / APIs)
- Modular architecture

## Tech Stack
- Python
- Telethon
- SQLite
- REST APIs (Webhooks)

## How It Works
Telegram → Telethon Client → Processor → Database → Webhook

## Installation

```bash
git clone https://github.com/yourusername/telegram-automation-pipeline
cd telegram-automation-pipeline
pip install -r requirements.txt
```

## Setup

Create .env file:
- API_ID=xxxx
- API_HASH=xxxx
- PHONE=xxxx
- CHANNEL_USERNAME=@channel
- WEBHOOK_URL=https://****.com

## Run Project
```
python main.py
```

## Output
- Stores messages in SQLite database
- Prints processed messages in terminal
- Sends webhook payload if configured

## Use Cases
- Telegram monitoring systems
- Crypto signal automation
- Notification pipelines
- Data ingestion systems

## Author

Automation & DevOps Engineer (Python / CI-CD / API Integrations)
