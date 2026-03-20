import argparse
import asyncio
import sys
import logging
from aiogram import Bot, Dispatcher, types

# Import your config and isolated core logic
import config
from handlers.commands import handle_command

# Initialize the Telegram dispatcher
dp = Dispatcher()


@dp.message()
async def universal_handler(message: types.Message):
    """
    Catches messages, passes them to our isolated handler logic,
    and sends the response back to the user in Telegram.
    """
    # If the message has text, process it through our core logic
    if message.text:
        response = handle_command(message.text)
        await message.answer(response)


async def main():
    # 1. Handle CLI arguments for test mode
    parser = argparse.ArgumentParser(description="LMS Telegram Bot")
    parser.add_argument("--test", type=str, help="Run a command in test mode without Telegram")
    args = parser.parse_args()

    # If --test flag is provided, run offline mode and exit
    if args.test:
        response = handle_command(args.test)
        print(response)
        sys.exit(0)

    # 2. Run real Telegram bot if no --test flag
    if not config.BOT_TOKEN:
        print("Error: BOT_TOKEN is missing. Check your .env.bot.secret file at the project root.")
        sys.exit(1)

    # Enable logging to see bot activity in the terminal
    logging.basicConfig(level=logging.INFO)

    # Initialize bot and start polling
    bot = Bot(token=config.BOT_TOKEN)
    print("Starting Telegram bot polling...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())