import asyncio
from aiogram import Bot, Dispatcher
from config1 import TOKEN
from user_handlers import register_user_handlers
from admin_handlers import register_admin_handlers

bot = Bot(token=TOKEN)
dp = Dispatcher()

register_user_handlers(dp)
register_admin_handlers(dp)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

