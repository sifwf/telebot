import asyncio
from aiogram import Bot, Dispatcher
from handlers.main_handlers import router
from handlers.router import router1
from config import BOT

bot = Bot(token=BOT)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    dp.include_router(router1)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())