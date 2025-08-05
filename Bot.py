import logging
from telegram.ext import Application, CommandHandler
from handlers import start, help_command, profile
from db import create_tables
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

def main():
    create_tables()
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("profile", profile))

    app.run_polling()

if __name__ == "__main__":
    main()
