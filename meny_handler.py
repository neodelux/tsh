from telegram.ext import MessageHandler, filters
from telegram import Update, ContextTypes
from bot.utils.logger import get_logger
from bot.utils.helpers import safe_send_message

logger = get_logger(__name__)

menu_buttons_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu_buttons)

async def handle_menu_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text
    logger.info(f"User {user.id} pressed button: {text}")
    await safe_send_message(context, user.id, f"You pressed: {text}")
