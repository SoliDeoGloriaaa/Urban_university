from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv('API_KEY')

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Calories', state='*')
async def set_age(message, state):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)

    data = await state.get_data()
    
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    
    calories = 10 * weight + 6.25 * growth - 5 * age + 5
    
    await message.answer(f'Ваша норма калорий: {calories} ккал.')
    
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)