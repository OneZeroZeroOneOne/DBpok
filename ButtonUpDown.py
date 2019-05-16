import settings
import sqlite3
from aiogram.types import ReplyKeyboardRemove, \
ReplyKeyboardMarkup, InlineKeyboardMarkup, \
InlineKeyboardButton
def ButtnUPDOWN(IdPokemon):
    conn = sqlite3.connect("{}".format(settings.poke_db))
    cursor = conn.cursor()
    markup = InlineKeyboardMarkup()
    weeklist = list()
    for i in range(0,6,1):
        sample = cursor.execute("SELECT * FROM PokemonDB WHERE PokemonID = {}".format(str(IdPokemon+i)))
        sample = cursor.fetchone()
        weeklist.append(InlineKeyboardButton("{}".format(sample[2]), callback_data = "ID:"+sample[1]))
    markup.row(*weeklist)
    inline_Nazas = InlineKeyboardButton("Назад", callback_data='UP')
    inline_Vpered = InlineKeyboardButton("Вперед", callback_data='DOWN')
    markup.add(inline_Nazad,inline_Vpered)
    return sample[2]
    
