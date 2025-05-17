from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update
from bot.utils.helpers import safe_send_message
from bot.utils.logger import get_logger

logger = get_logger(__name__)
admin_broadcast_states = {}

admin_broadcast_handler = CommandHandler("sendsendadminlol", start_admin_broadcast)
admin_message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND & filters.User(user_id=ADMIN_ID), handle_admin_message)
cancel_broadcast_handler = CommandHandler("cancel_broadcast", cancel_broadcast)
reset_state_handler = CommandHandler("reset_state", reset_admin_state)

async def start_admin_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user.id != ADMIN_ID:
        await safe_send_message(context, user.id, "❌ Only admin can use this command.")
        return
    admin_broadcast_states[user.id] = "waiting_for_message"
    await safe_send_message(context, user.id, "📢 Enter your broadcast message:")

async def handle_admin_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user.id not in admin_broadcast_states:
        return
    msg = update.message.text
    logger.info(f"📢 Admin {user.id} sent broadcast: {msg}")
    await safe_send_message(context, user.id, f"📢 Broadcast sent: {msg}")
    del admin_broadcast_states[user.id]

async def cancel_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user.id in admin_broadcast_states:
        del admin_broadcast_states[user.id]
    await safe_send_message(context, user.id, "❌ Broadcast cancelled.")

async def reset_admin_state(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user.id != ADMIN_ID:
        return
    admin_broadcast_states.clear()
    await safe_send_message(context, user.id, "✅ Admin state cleared.")
