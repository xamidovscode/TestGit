import asyncio
from aiogram import Dispatcher, Bot, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton
from translations import TRANSLATION
from texts import languages_text

bot = Bot(token='7944749152:AAHTbw9ojY1YQ7TE9QbYXJ2SaFfZOnNUELs')
dp = Dispatcher()

language = "ru"

@dp.message(Command("start"))
async def catch_command(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uzb"), InlineKeyboardButton(text="🇷🇺 Rусский", callback_data="rus"), InlineKeyboardButton(text="🇺🇸 English", callback_data="eng")]
        ],
    )
    await message.answer(languages_text, reply_markup=keyboard)

@dp.callback_query(lambda message: message.data == "rus")
async def set_language(callback_query):
    await callback_query.message.answer("Привет!")

@dp.message()
async def set_language(message: Message):
    await message.answer(TRANSLATION[language]['salom'])

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



