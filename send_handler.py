from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
from bot.utils.helpers import safe_send_message
from bot.utils.logger import get_logger

logger = get_logger(__name__)

send_command_handler = CommandHandler("send", send_tsh)

async def send_tsh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    args = context.args
    if len(args) != 2:
        await safe_send_message(context, user.id, "Usage: /send [user_id] [amount]")
        return
    target_id, amount = args[0], args[1]
    await safe_send_message(context, user.id, f"📩 Sending {amount} TSH to {target_id}")
