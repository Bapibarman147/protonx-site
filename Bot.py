import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler
from handlers import *

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("profile", profile))
    dp.add_handler(CommandHandler("balance", balance))
    dp.add_handler(CommandHandler("refer", refer))
    dp.add_handler(CommandHandler("setwallet", setwallet))
    dp.add_handler(CommandHandler("dailybonus", dailybonus))
    dp.add_handler(CommandHandler("withdraw", withdraw))

    PORT = int(os.environ.get('PORT', 8443))
    updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"https://protonx-bot.onrender.com/{TOKEN}"
    )

    print("🚀 Bot running...")
    updater.idle()

if __name__ == "__main__":
    main()
