from aiogram import Dispatcher, types, executor, Bot
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging

from db import add_user, add_user_name, add_user_team, get_user_name, get_user_team

bot = Bot("6156241028:AAGeYMYXby560yzIl6YuMRZpsn_YFDXntOk")
dp = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(level=logging.INFO)


class user_reg(StatesGroup):
    name = State()
    team = State()



@dp.message_handler(state=user_reg.name)
async def add_name(message: types.Message, state: FSMContext):
    # chat_id = message.chat.id
    user_name = message.text

    await state.update_data(user_name=user_name)
    await user_reg.team.set()

    keyboard = InlineKeyboardMarkup(row_width=2)
    button_bear = InlineKeyboardButton("Отряд BEAR", callback_data='cal_BEAR')
    button_usec = InlineKeyboardButton("Отряд USEC", callback_data='cal_USEC')
    keyboard.add(button_bear, button_usec)

    await message.answer('Выберите отряд (BEAR/USEC)', reply_markup=keyboard)


@dp.message_handler(state=user_reg.team)
async def add_name(message: types.Message, state=FSMContext):
    chat_id = message.chat.id
    await state.finish()
    add_user_team(message)
    await bot.send_message(chat_id, "Регистрация завершена.")


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message, state=FSMContext):
    chat_id = message.chat.id
    user_register = add_user(message)
    if user_register == False:
        await bot.send_message(chat_id, "Вы уже зарегистрированы. Используйте команду /profile!")
    else:
        await bot.send_message(chat_id,
                               f"Добро пожаловать в Телеграм-версию игры Escape From Tarkov, {message.from_user.full_name} ! \n \n"
                               f"Введите никнейм : ")
        await user_reg.name.set()


@dp.message_handler(commands=['profile'])
async def start_message(message: types.Message, state=FSMContext):
    chat_id = message.from_user.id
    user_name = get_user_name(chat_id)
    user_team = get_user_team(chat_id)
    await message.answer("ЛИЧНЫЙ ПРОФИЛЬ \n \n"
                         f"Ваш никнейм : {user_name} \n"
                         f"Отряд : {user_team} \n"
                         f"Баланс : Тестируется")


if __name__ == '__main__':
    executor.start_polling(dp)
