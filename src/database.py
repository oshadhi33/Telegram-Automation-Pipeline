import sqlite3
from datetime import datetime
from config import DB_NAME

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message_id TEXT,
            sender TEXT,
            message TEXT,
            created_at TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_message(self, message_id, sender, message):
        query = """
        INSERT INTO messages (message_id, sender, message, created_at)
        VALUES (?, ?, ?, ?)
        """
        self.conn.execute(query, (
            message_id,
            sender,
            message,
            datetime.now().isoformat()
        ))
        self.conn.commit()
