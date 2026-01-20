import sqlite3
from config import DB_NAME

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS reminders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER,
                text TEXT,
                remind_time TEXT
            )
        """)

def add_reminder(chat_id, text, remind_time):
    with connect() as conn:
        conn.execute(
            "INSERT INTO reminders (chat_id, text, remind_time) VALUES (?, ?, ?)",
            (chat_id, text, remind_time)
        )

def get_due_reminders(now):
    with connect() as conn:
        return conn.execute(
            "SELECT id, chat_id, text FROM reminders WHERE remind_time <= ?",
            (now,)
        ).fetchall()

def delete_reminder(reminder_id):
    with connect() as conn:
        conn.execute(
            "DELETE FROM reminders WHERE id = ?",
            (reminder_id,)
        )
