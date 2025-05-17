from telegram import ContextTypes, Update
from telegram.error import RetryAfter
from bot.utils.logger import get_logger

logger = get_logger(__name__)

async def safe_send_message(context: ContextTypes.DEFAULT_TYPE, chat_id: int, text: str, parse_mode: str = "MarkdownV2"):
    try:
        await context.bot.send_message(chat_id=chat_id, text=text, parse_mode=parse_mode)
    except RetryAfter as e:
        logger.warning(f"⚠️ Flood control for {chat_id}: {e}")
        await asyncio.sleep(e.retry_after)
        await context.bot.send_message(chat_id=chat_id, text=text, parse_mode=parse_mode)
    except Exception as e:
        logger.error(f"🔴 Error sending message to {chat_id}: {e}")
