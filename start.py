from telegram.ext import CommandHandler
from telegram import Update, ContextTypes
from bot.utils.logger import get_logger
from bot.utils.helpers import safe_send_message

logger = get_logger(__name__)

start_command_handler = CommandHandler("start", start)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("User started the bot")
    await safe_send_message(context, update.effective_user.id, "Welcome to TSH Bot!")
