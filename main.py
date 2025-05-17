import os
import asyncio
from telegram.ext import Application
from dotenv import load_dotenv
from bot.handlers import (
    start_handler,
    menu_handler,
    send_handler,
    mining_handler,
    admin_handler
)
from bot.utils import logger

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("❌ BOT_TOKEN not found in .env")

async def main():
    application = Application.builder().token(TOKEN).build()
    
    # Register handlers
    application.add_handler(start_handler.start_command_handler)
    application.add_handler(menu_handler.menu_buttons_handler)
    application.add_handler(send_handler.send_command_handler)
    application.add_handler(mining_handler.mining_command_handler)
    application.add_handler(mining_handler.stop_mining_handler)
    application.add_handler(admin_handler.admin_broadcast_handler)
    application.add_handler(admin_handler.admin_message_handler)
    application.add_handler(admin_handler.cancel_broadcast_handler)
    application.add_handler(admin_handler.reset_state_handler)

    logger.info("🚀 Bot started")
    await application.initialize()
    await application.start()
    await application.updater.start_polling()

    try:
        while True:
            await asyncio.sleep(3600)
    except (KeyboardInterrupt, asyncio.CancelledError):
        logger.info("🛑 Bot stopping...")
        await application.stop()
        logger.info("✅ Bot stopped")

if __name__ == '__main__':
    asyncio.run(main())
