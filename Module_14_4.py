from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *

api = '8128934102:AAG6Q7YaItHyG23xE30uJTsOjT4zfyBRgOc'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_kb_1 = KeyboardButton(text='Рассчитать')
button_kb_2 = KeyboardButton(text='Информация')
button_kd_3 = KeyboardButton(text='Купить')
kb.row(button_kb_1, button_kb_2)
kb.add(button_kd_3)

kb1 = InlineKeyboardMarkup(resize_keyboard=True)
button_kb1_1 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')
button_kb1_2 = InlineKeyboardButton(text="Формулы расчёта", callback_data='formulas')
kb1.add(button_kb1_1)
kb1.add(button_kb1_2)

kb3 = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text='Продукт1', callback_data='product_buying'),
        InlineKeyboardButton(text='Продукт2', callback_data='product_buying'),
        InlineKeyboardButton(text='Продукт3', callback_data='product_buying'),
        InlineKeyboardButton(text='Продукт4', callback_data='product_buying')
    ],
])

initiate_db(4)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text=['Информация'])
async def info(message):
    await message.answer('Информация о боте!')

@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for i in range(1, 5):
        pr = get_all_products(i)
        await message.answer(f'Название: {pr[1]} | Описание: {pr[2]} | Цена: {pr[3]}')
        with open(f'C:/Users\Serg\PycharmProjects\pythonProject1/urban\Module14\picture{i}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=kb3)

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
     await message.answer('Выберите опцию:', reply_markup=kb1)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формула Миффлина - Сан Жеора: 10*вес(кг) + 6,25*рост(см) – 5*возраст(лет) + 5')
    # await call.message()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    # await call.message()
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age_=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth_=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight_=message.text)
    data = await state.get_data()
    await message.answer(f'Возраст: {data["age_"]}, рост: {data["growth_"]}, вес: {data["weight_"]}')
    calories = 10 * int(data["weight_"]) + 6.25 * int(data["growth_"]) - 5 * int(data["age_"]) + 5
    await message.answer(f'Ваша норма каллорий: {calories}')
    await state.finish()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)