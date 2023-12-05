from config import TOKEN

from aiogram import Bot, Dispatcher

if __name__ == "__main__":
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.start_polling(bot)
