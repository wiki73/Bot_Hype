import asyncio

from aiogram import Bot, Dispatcher
from handlers import router
from config import bot_token

bot = Bot(token=bot_token)

dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
