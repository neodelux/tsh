from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
from bot.utils.helpers import safe_send_message
from bot.utils.logger import get_logger

logger = get_logger(__name__)

mining_sessions = {}

mining_command_handler = CommandHandler("mine", start_mining)

async def start_mining(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user.id in mining_sessions:
        await safe_send_message(context, user.id, "⏳ You're already mining.")
        return
    logger.info(f"⛏ Mining started for user {user.id}")
    mining_sessions[user.id] = True
    await safe_send_message(context, user.id, "⛏ Mining started...")

stop_mining_handler = CommandHandler("stop_mining", stop_mining)

async def stop_mining(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user.id in mining_sessions:
        del mining_sessions[user.id]
        await safe_send_message(context, user.id, "⏹ Mining stopped manually.")
    else:
        await safe_send_message(context, user.id, "🛑 You are not currently mining.")
