from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from dotenv import load_dotenv
from crud_functions import initiate_db, get_all_products
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


def create_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.KeyboardButton('Рассчитать'),
        types.KeyboardButton('Информация'),
        types.KeyboardButton('Купить')
    ]
    keyboard.add(*buttons)
    return keyboard


def create_inline_keyboard():
    inline_keyboard = types.InlineKeyboardMarkup()
    button_calories = types.InlineKeyboardButton(
        text='Рассчитать норму калорий',
        callback_data='calories'
    )
    button_formulas = types.InlineKeyboardButton(
        text='Формулы расчёта',
        callback_data='formulas'
    )
    inline_keyboard.add(button_calories, button_formulas)
    return inline_keyboard


def create_product_inline_keyboard():
    inline_keyboard = types.InlineKeyboardMarkup()
    products = ['Product1', 'Product2', 'Product3', 'Product4']
    for product in products:
        button = types.InlineKeyboardButton(
            text=product,
            callback_data='product_buying'
        )
        inline_keyboard.add(button)
    return inline_keyboard


@dp.message_handler(commands=['start'])
async def start(message):
    keyboard = create_keyboard()
    await message.answer(
        'Привет! Я бот, помогающий твоему здоровью.', reply_markup=keyboard
    )


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    inline_keyboard = create_inline_keyboard()
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    if not products:
        await message.answer("Нет доступных продуктов.")
        return
    img_number = 0
    for title, description, price in products:
        await message.answer(f'Название: {title} | Описание: {description} | Цена: {price}')
        with open(f'image/{img_number + 1}img.jpg', 'rb') as photo:
            await bot.send_photo(message.chat.id, photo)
        img_number += 1


@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call):
    formula_message = (
        "Формула Миффлина-Сан Жеора:\n"
        "Для мужчин: BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(годы) + 5\n"
        "Для женщин: BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(годы) - 161"
    )
    await call.message.answer(formula_message)


@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call):
    await UserState.age.set()
    await call.message.answer("Введите свой возраст:")


@dp.message_handler(state=UserState.age)
async def process_age(message, state):
    age = message.text
    await state.update_data(age=age)
    await UserState.next()
    await message.answer("Введите свой рост:")


@dp.message_handler(state=UserState.growth)
async def process_growth(message, state):
    growth = message.text
    await state.update_data(growth=growth)
    await UserState.next()
    await message.answer("Введите свой вес:")


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
    initiate_db()
    executor.start_polling(dp, skip_updates=True)
