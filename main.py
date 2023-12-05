import asyncio
from config import TOKEN
from aiogram import Bot, Dispatcher
from Core.routers.basic_router import basic_router


async def main():
    bot = Bot(TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(basic_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
