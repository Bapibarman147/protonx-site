from telegram import Update
from telegram.ext import CallbackContext
from datetime import datetime, timedelta
from database import *

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    ref = context.args[0] if context.args else None
    ref_id = int(ref) if ref and ref.isdigit() else None

    add_user(user.id, ref_id)
    context.bot.send_message(chat_id=user.id,
        text="🎉 Welcome to ProtonX Bot!\nUse /help to explore commands.")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("""
📜 Commands:
• /profile - View profile
• /balance - Check balance
• /refer - Get your referral link
• /setwallet [address] - Set wallet
• /dailybonus - Claim daily bonus
• /withdraw - Request withdrawal
""")

def profile(update: Update, context: CallbackContext):
    user = get_user(update.effective_user.id)
    if user:
        _, join_date, balance, referrals, wallet, ref_by, _ = user
        update.message.reply_text(f"""
👤 Profile:
📅 Joined: {join_date}
💰 Balance: {balance} PX
👥 Referrals: {referrals}
🏦 Wallet: {wallet or "Not set"}
""")

def balance(update: Update, context: CallbackContext):
    user = get_user(update.effective_user.id)
    update.message.reply_text(f"💰 Your balance: {user[2]} PX")

def refer(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    update.message.reply_text(f"🔗 Your referral link:\nhttps://t.me/Protonxairdrop_bot?start={user_id}")

def setwallet(update: Update, context: CallbackContext):
    if context.args:
        wallet = context.args[0]
        set_wallet(update.effective_user.id, wallet)
        update.message.reply_text("✅ Wallet set successfully!")
    else:
        update.message.reply_text("❌ Usage: /setwallet [your_wallet_address]")

def dailybonus(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user = get_user(user_id)
    now = datetime.utcnow()
    last_claim = datetime.strptime(user[6], "%Y-%m-%d %H:%M:%S")

    if now - last_claim >= timedelta(days=1):
        update_balance(user_id, 10)
        update_last_bonus(user_id, now.strftime("%Y-%m-%d %H:%M:%S"))
        update.message.reply_text("🎁 You received 10 PX daily bonus!")
    else:
        wait_time = (last_claim + timedelta(days=1)) - now
        hours = int(wait_time.total_seconds() // 3600)
        minutes = int((wait_time.total_seconds() % 3600) // 60)
        update.message.reply_text(f"⏳ Come back in {hours}h {minutes}m for next bonus.")

def withdraw(update: Update, context: CallbackContext):
    user = get_user(update.effective_user.id)
    if not user[4]:
        update.message.reply_text("❌ Please set your wallet using /setwallet first.")
    elif user[2] < 100:
        update.message.reply_text("🚫 Minimum 100 PX required to withdraw.")
    else:
        update.message.reply_text("✅ Withdrawal request received! Team will process it soon.")
