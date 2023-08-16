from db import add_user, add_user_name, add_user_team, get_user_name, get_user_team
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram import Dispatcher

# @dp.message_handler(commands=['profile'])
async def start_message(message: types.Message, state=FSMContext):
    chat_id = message.from_user.id
    user_name = get_user_name(chat_id)
    user_team = get_user_team(chat_id)
    await message.answer("ЛИЧНЫЙ ПРОФИЛЬ \n \n"
                                    f"Ваш никнейм : {user_name} \n"
                                    f"Отряд : {user_team} \n"
                                    f"Баланс : Тестируется")

def register_handlers_profile(dp : Dispatcher):
    dp.register_message_handler(start_message, command=['profile'])