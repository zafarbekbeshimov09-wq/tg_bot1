import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiohttp import web

# Telegram @BotFather'dan olgan tokeningiz
BOT_TOKEN = "8866966342:AAGL6S-AQEzKXznR4SM0UYB_K2XnDVI0Pg0"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def get_main_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="1. Uzum Bankdan pul ishlash 💳", 
                    url="https://b.2u.uz/ref?c=50&a=80gStOUiuc"
                )
            ],
            [
                InlineKeyboardButton(
                    text="2. Har soniyada pul ishlash ⚡", 
                    url="https://t.me/cointbot_bit_bot?start=ref_1621504_g95"
                )
            ],
            [
                InlineKeyboardButton(
                    text="3. MLBB tekin olmos 💎", 
                    url="https://diamonds.b4a.app/?uid=bxJb43SD6V"
                )
            ],
            # 🔽 YANGI 4-HAVOLA SHU YERGA QO'SHILDI 🔽
            [
                InlineKeyboardButton(
                    text="4. har soatda 100ming 📢", 
                    url="https://tronpick.io/?ref=zafarbek_8bd"
                )
            ]
        ]
    )

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    welcome_text = f"Xush kelibsiz, {message.from_user.full_name}!\n\nQuyidagi bo'limlardan birini tanlang:"
    await message.answer(welcome_text, reply_markup=get_main_keyboard())

async def handle_ping(request):
    return web.Response(text="Bot ishlayapti!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

async def main():
    logging.basicConfig(level=logging.INFO)
    await start_web_server()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
