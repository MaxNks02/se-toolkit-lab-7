import argparse
import asyncio
import sys
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from handlers.core.commands import handle_command

dp = Dispatcher()

# P1.3: Inline keyboard buttons setup
def get_start_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📚 Labs", callback_data="ask_labs")],
        [InlineKeyboardButton(text="🏥 Health", callback_data="ask_health")]
    ])

@dp.message()
async def universal_handler(message: types.Message):
    if message.text:
        response = handle_command(message.text)
        if message.text.strip().lower().startswith("/start"):
            await message.answer(response, reply_markup=get_start_keyboard())
        else:
            await message.answer(response)

@dp.callback_query(F.data.startswith("ask_"))
async def handle_callback(callback: types.CallbackQuery):
    if callback.data == "ask_labs":
        response = handle_command("what labs are available")
    elif callback.data == "ask_health":
        response = handle_command("/health")
    await callback.message.answer(response)
    await callback.answer()

# P1.3: Inline keyboard buttons setup
# P1.3: Inline keyboard buttons setup
async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", type=str)
    args = parser.parse_args()

    if args.test:
        response = handle_command(args.test)
        print(response)
        sys.exit(0)

    bot = Bot(token=config.BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
