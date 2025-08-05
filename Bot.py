import os
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
from database import add_user, get_user, get_balance

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    user = update.effective_user
    user_id = user.id
    username = user.username or "NoUsername"
    args = context.args
    referred_by = int(args[0]) if args else None

    add_user(user_id, username, referred_by)
    context.bot.send_message(chat_id=user_id, text="🎉 Welcome to ProtonX Airdrop!\nUse /help to see all commands.")

def help_command(update, context):
    update.message.reply_text(
        "📌 Commands:\n"
        "/start - Join the bot\n"
        "/profile - View your details\n"
        "/balance - Check your balance\n"
        "/refer - Get your referral link\n"
        "/help - Show this message"
    )

def profile(update, context):
    user_id = update.effective_user.id
    user_data = get_user(user_id)
    if user_data:
        _, username, join_date, balance, referred_by, referrals = user_data
        update.message.reply_text(
            f"👤 Profile:\n"
            f"🆔 ID: {user_id}\n"
            f"📛 Username: @{username}\n"
            f"🗓️ Joined: {join_date}\n"
            f"💰 Balance: {balance} PX\n"
            f"👥 Referrals: {referrals}"
        )
    else:
        update.message.reply_text("❌ You are not registered.")

def balance(update, context):
    user_id = update.effective_user.id
    bal = get_balance(user_id)
    update.message.reply_text(f"💰 Your balance: {bal} PX")

def refer(update, context):
    user_id = update.effective_user.id
    update.message.reply_text(
        f"🔗 Share your referral link:\n"
        f"https://t.me/Protonxairdrop_bot?start={user_id}"
    )

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start, pass_args=True))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("profile", profile))
    dp.add_handler(CommandHandler("balance", balance))
    dp.add_handler(CommandHandler("refer", refer))

    port = int(os.environ.get("PORT", "8443"))
    updater.start_webhook(
        listen="0.0.0.0",
        port=port,
        url_path=TOKEN,
        webhook_url=f"https://protonx-bot.onrender.com/{TOKEN}"
    )
    updater.idle()

if __name__ == "__main__":
    main()
