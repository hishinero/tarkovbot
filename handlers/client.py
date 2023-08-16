from aiogram import Dispatcher, types
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from helper import bot, dp

from db import add_user, add_user_name, add_user_team, get_user_name, get_user_team

class user_reg(StatesGroup):
    name = State()
    team = State()

# @dp.message_handler(state=user_reg.name)
async def add_name(message:types.Message,state=FSMContext):
    chat_id = message.chat.id
    await state.finish()
    add_user_name(message)
    await bot.send_message(chat_id, "Выберите отряд (BEAR/USEC)")
    await user_reg.team.set()

# @dp.message_handler(state=user_reg.team)
async def add_name(message:types.Message,state=FSMContext):
    chat_id = message.chat.id
    await state.finish()
    add_user_team(message)
    await bot.send_message(chat_id, "Регистрация завершена.")


# @dp.message_handler(commands=['start'])
async def command_start(message:types.Message,state=FSMContext):
    chat_id = message.chat.id
    user_register = add_user(message)
    if user_register == False:
        await bot.send_message(chat_id, "Вы уже зарегистрированы. Используйте команду /profile!")
    else:
        await bot.send_message(chat_id, f"Добро пожаловать в Телеграм-версию игры Escape From Tarkov, {message.from_user.full_name} ! \n \n"
                                    f"Введите никнейм : ")
        await user_reg.name.set()

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, command=['start'])
    dp.register_message_handler(add_name)
