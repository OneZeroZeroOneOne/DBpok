token = "858185563:AAEIh49GYHAEGb_1PK4K2VQuFftBto5zEpU"
import sqlite3
import settings
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
ReplyKeyboardMarkup, InlineKeyboardMarkup, \
InlineKeyboardButton
import random

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['pokemon'])
async def process_start_command(message: types.Message):
    argument = message.get_args()
    if argument[0].isdigit():
        conn = sqlite3.connect("{}".format(settings.poke_db))
        cursor = conn.cursor()
        sample = cursor.execute("SELECT * FROM PokemonDB WHERE PokemonID = '{}'".format(argument))
        sample = cursor.fetchone()
        strng = "*Имя покемона:* {}\n*В общем:* {}\n*Атака:* {}\n*HP:* {}\n*Защита:* {}\n*Тип1:* {}\n*Тип2:* {}\n*Ск.Атк:* {}\n"\
        "*Cк.Защ:* {}\n*Скорость:* {}\n*Поколение:* {}\n*Легендарность:* {}\n*ID:* {}".format(sample[2],sample[5],sample[7],sample[6],\
        sample[8],sample[3],sample[4],sample[9],sample[10],sample[11],sample[12],sample[13],sample[1])
        print(*sample)
        await bot.send_photo(chat_id = message.chat.id, \
        photo = types.InputFile("pokemons_img\{}#{}.jpg".format(sample[1],sample[2].lower()))\
        , caption = strng, parse_mode = 'Markdown')

if __name__ == "__main__":
    executor.start_polling(dp)
