from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.row(button1, button2)

kb1 = InlineKeyboardMarkup(resize_keyboard=True)
button3 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')
button4 = InlineKeyboardButton(text="Формулы расчёта", callback_data='formulas')
kb1.add(button3)
kb1.add(button4)

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

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
     await message.answer('Выберите опцию:', reply_markup=kb1)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формула Миффлина - Сан Жеора: 10*вес(кг) + 6,25*рост(см) – 5*возраст(лет) + 5')
    await call.message()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.message()
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
    # await message.answer(f'Возраст: {data["age_"]}, рост: {data["growth_"]}, вес: {data["weight_"]}')
    calories = 10 * int(data["weight_"]) + 6.25 * int(data["growth_"]) - 5 * int(data["age_"]) + 5
    await message.answer(f'Ваша норма каллорий: {calories}')
    await state.finish()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)