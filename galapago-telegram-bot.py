import asyncio
import nest_asyncio
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, InputFile
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
LOGO_URL = 'https://galapago.app/wp-content/uploads/2022/05/coin.png'  # URL to your logo image
DESCRIPTION = """
Welcome to Project Galapago Telegram Bot!
This bot allows you to access our web app directly from Telegram.

Features:
- Easy access to our web app
- Real-time updates
- Seamless integration

Click the button below to get started!
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Create an inline keyboard with a button that opens the web app
    keyboard = [
        [InlineKeyboardButton("Open Web App", web_app=WebAppInfo(url="https://testnet.galapago.app"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send logo image with description and inline keyboard in a single message
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=LOGO_URL,
        caption=DESCRIPTION,
        reply_markup=reply_markup
    )

async def main():
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TOKEN).build()

    # Add a handler for the /start command
    application.add_handler(CommandHandler('start', start))

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    await application.run_polling()

if __name__ == '__main__':
    nest_asyncio.apply()
    asyncio.run(main())
