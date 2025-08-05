from telegram import Update
from telegram.ext import ContextTypes
from db import add_user, get_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ref_by = None
    if context.args:
        try:
            ref_by = int(context.args[0])
        except:
            pass
    user = update.effective_user
    add_user(user.id, ref_by)
    await update.message.reply_text(f"👋 হ্যালো {user.first_name}, ProtonX-এ তোমাকে স্বাগতম!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🆘 সাহায্য:\n/start - শুরু করুন\n/profile - আপনার প্রোফাইল দেখুন")

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.effective_user.id)
    if user:
        msg = f"""👤 আপনার প্রোফাইল:
🆔 ID: {user[0]}
📅 যোগদানের তারিখ: {user[1]}
💰 ব্যালেন্স: {user[2]} ৳
👥 রেফারেল: {user[3]}
📥 রেফার্ড বাই: {user[5]}
💼 Wallet: {user[4] or 'Not set'}
"""
        await update.message.reply_text(msg)
    else:
        await update.message.reply_text("প্রোফাইল পাওয়া যায়নি। /start দিন।")
