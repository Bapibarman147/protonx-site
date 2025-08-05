import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers import start, help_command, profile
from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Database initialize
conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    balance INTEGER DEFAULT 0,
    referrals INTEGER DEFAULT 0,
    join_date TEXT
)
""")
conn.commit()
conn.close()

# Logging
logging.basicConfig(level=logging.INFO)

# Bot setup
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("profile", profile))

app.run_polling()
