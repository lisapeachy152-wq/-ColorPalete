import logging
import sys
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from config import Config
from handlers import BotHandlers

# Add the current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    """Start the bot"""
    try:
        # Validate configuration
        Config.validate()
        
        # Create application
        application = Application.builder().token(Config.BOT_TOKEN).build()
        
        # Initialize handlers
        handlers = BotHandlers()
        
        # Add command handlers
        application.add_handler(CommandHandler("start", handlers.start_command))
        application.add_handler(CommandHandler("help", handlers.help_command))
        application.add_handler(CommandHandler("list", handlers.list_palettes_command))
        application.add_handler(CommandHandler("palette", handlers.palette_command))
        application.add_handler(CommandHandler("color", handlers.color_command))
        application.add_handler(CommandHandler("harmony", handlers.harmony_command))
        
        # Add message handler for text
        application.add_handler(MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handlers.handle_message
        ))
        
        # Add callback handler for inline buttons
        application.add_handler(CallbackQueryHandler(handlers.callback_handler))
        
        # Start the bot
        logger.info("🎨 Color Palette Bot is starting...")
        application.run_polling(allowed_updates=Update.ALL_TYPES)
        
    except Exception as e:
        logger.error(f"❌ Error starting bot: {e}")
        raise

if __name__ == '__main__':
    main()
