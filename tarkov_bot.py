from aiogram.utils import executor
from helper import dp

async def on_startup( ):
    print('Бот вышел в онлайн!')

from handlers import client, profile, db

client.register_handlers_client(dp)
profile.register_handlers_client(dp)
db.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True)