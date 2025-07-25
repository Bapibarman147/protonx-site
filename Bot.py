import os
from telegram.ext import Updater, CommandHandler

# Bot token (hardcoded for now, but use environment variable in Render)
TOKEN = "8075686130:AAFiewbewwwrq4SDIXle0aUPZCGxtuA3l7s"

# Command handlers
def start(update, context):
    user_id = update.effective_user.id
    welcome_message = "🎉 Welcome to ProtonX Bot! Start your journey with us. Use /help for commands."
    context.bot.send_message(chat_id=user_id, text=welcome_message)

def help_command(update, context):
    user_id = update.effective_user.id
    help_text = "Available commands:\n/start - Start the bot\n/tokenomics - View ProtonX token distribution\n/slogan - Get our slogan\n/links - Get all ProtonX links\n/help - Show this message"
    context.bot.send_message(chat_id=user_id, text=help_text)

def tokenomics(update, context):
    user_id = update.effective_user.id
    tokenomics_text = """
📊 ProtonX Tokenomics:
• Owner: 15%
• Airdrop: 15%
• Liquidity: 45%
• Development: 15%
• Game: 10%
"""
    context.bot.send_message(chat_id=user_id, text=tokenomics_text)

def slogan(update, context):
    user_id = update.effective_user.id
    slogan_text = "🚀 Slogan: Build from Zero — Rise to the Future"
    context.bot.send_message(chat_id=user_id, text=slogan_text)

def links(update, context):
    user_id = update.effective_user.id
    links_text = """
🌐 Website: https://bapibarman147.github.io/protonx-site/
✈️ Telegram: https://t.me/protonxofficial
🎥 YouTube: https://www.youtube.com/@ProtonXofficial
📘 Facebook: https://www.facebook.com/share/1CF1A6qXjw/
"""
    context.bot.send_message(chat_id=user_id, text=links_text)

# Bot setup
def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("tokenomics", tokenomics))
    dp.add_handler(CommandHandler("slogan", slogan))
    dp.add_handler(CommandHandler("links", links))

    # Webhook setup for 24/7 operation on Render
    port = int(os.getenv('PORT', 10000))
    updater.start_webhook(
        listen='0.0.0.0',
        port=port,
        url_path=TOKEN,
        webhook_url=f'https://protonx-bot.onrender.com/{TOKEN}'
    )
    print(f"Webhook set to https://protonx-bot.onrender.com/{TOKEN}")
    updater.idle()

if __name__ == '__main__':
    main()
