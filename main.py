import asyncio
from aiogram import Bot, Dispatcher
from handlers.main_handlers import router
from handlers.router import router1
from handlers.router1 import router2
from config import BOT

bot = Bot(token=BOT)
dp = Dispatcher()

print("hello world")

async def main():
    dp.include_router(router)
    dp.include_router(router1)
    dp.include_router(router2)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())