token = "858185563:AAEIh49GYHAEGb_1PK4K2VQuFftBto5zEpU"
import sqlite3
import settings
import ButtonUpDown
import DBworker
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
async def process_pokemon_command(message: types.Message):
    argument = message.get_args()
    print(argument)
    if argument.isdigit():
        strng = "*Имя покемона:* {}\n*В общем:* {}\n*Атака:* {}\n*HP:* {}\n*Защита:* {}\n*Тип1:* {}\n*Тип2:* {}\n*Ск.Атк:* {}\n"\
        "*Cк.Защ:* {}\n*Скорость:* {}\n*Поколение:* {}\n*Легендарность:* {}\n*ID:* {}".format(DBworker.DB.Sample(argument,0)[2],DBworker.DB.Sample(argument,0)[5],DBworker.DB.Sample(argument,0)[7],DBworker.DB.Sample(argument,0)[6],\
        DBworker.DB.Sample(argument,0)[8],DBworker.DB.Sample(argument,0)[3],DBworker.DB.Sample(argument,0)[4],DBworker.DB.Sample(argument,0)[9],DBworker.DB.Sample(argument,0)[10],DBworker.DB.Sample(argument,0)[11],DBworker.DB.Sample(argument,0)[12],DBworker.DB.Sample(argument,0)[13],DBworker.DB.Sample(argument,0)[1])
        print(strng)
        await bot.send_photo(chat_id = message.chat.id, \
        photo = types.InputFile("pokemons_img\{}#{}.jpg".format(DBworker.DB.Sample(argument,0)[1],DBworker.DB.Sample(argument,0)[2].lower()))\
        , caption = strng, parse_mode = 'Markdown')

@dp.message_handler(commands=['pokemons'])
async def process_pokemons_command(message: types.Message):
    argument = message.get_args()
    print(argument)
    if argument.isdigit():
        markup = ButtonUpDown.ButtnUPDOWN(int(argument))
        await message.reply("Pokemon list",reply_markup = markup)
        
        


@dp.callback_query_handler()
async def query_InPok_proceed(call: types.CallbackQuery):
    strcalldata = call.data.split('/')
    argument = strcalldata[1]
    print(strcalldata[0],strcalldata[1],"ssssssssssssssss") 
    if strcalldata[0] == 'NAZ':
        markup = ButtonUpDown.ButtnUPDOWN(int(strcalldata[1])-11)
        await call.message.edit_text("Pokemon list", reply_markup = markup)   
    elif strcalldata[0] == 'NEXT':
        markup = ButtonUpDown.ButtnUPDOWN(int(strcalldata[1])+6)
        await call.message.edit_text("Pokemon list", reply_markup = markup)
    else:
        strng = "*Имя покемона:* {}\n*В общем:* {}\n*Атака:* {}\n*HP:* {}\n*Защита:* {}\n*Тип1:* {}\n*Тип2:* {}\n*Ск.Атк:* {}\n"\
        "*Cк.Защ:* {}\n*Скорость:* {}\n*Поколение:* {}\n*Легендарность:* {}\n*ID:* {}".format(DBworker.DB.Sample(argument,0)[2],DBworker.DB.Sample(argument,0)[5],DBworker.DB.Sample(argument,0)[7],DBworker.DB.Sample(argument,0)[6],\
        DBworker.DB.Sample(argument,0)[8],DBworker.DB.Sample(argument,0)[3],DBworker.DB.Sample(argument,0)[4],DBworker.DB.Sample(argument,0)[9],DBworker.DB.Sample(argument,0)[10],DBworker.DB.Sample(argument,0)[11],DBworker.DB.Sample(argument,0)[12],DBworker.DB.Sample(argument,0)[13],DBworker.DB.Sample(argument,0)[1])
        print(strng)
        await bot.send_photo(chat_id = call.from_user.id, \
        photo = types.InputFile("pokemons_img\{}#{}.jpg".format(DBworker.DB.Sample(argument,0)[1],DBworker.DB.Sample(argument,0)[2].lower()))\
        , caption = strng, parse_mode = 'Markdown')
        

if __name__ == "__main__":
    executor.start_polling(dp)
