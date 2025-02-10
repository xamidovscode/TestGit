import asyncio
from aiogram import Dispatcher, Bot, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile

bot = Bot(token='7944749152:AAHTbw9ojY1YQ7TE9QbYXJ2SaFfZOnNUELs')
dp = Dispatcher()

@dp.message(Command("start"))
async def catch_command(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📞 Bog'lanish uchun malumot", callback_data="connect")]
        ]
    )
    await message.answer("Salom sizga qanday yordam bera olaman", reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



