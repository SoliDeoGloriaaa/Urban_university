from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')
bot = Bot(token=api_key)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print('Привет! Я бот, помогающий твоему здоровью.')
    await message.reply('Привет! Я бот, помогающий твоему здоровью.')


@dp.message_handler()
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.reply('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
