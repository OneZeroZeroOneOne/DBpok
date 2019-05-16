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
    if IdPokemon < 1:
        IdPokemon = 1
    for i in range(0,6,1):
        sample = cursor.execute("SELECT * FROM PokemonDB WHERE PokemonID = {}".format(str(IdPokemon+i)))
        sample = cursor.fetchone()
        inl_but = InlineKeyboardButton("{}".format(sample[2]), callback_data = "ID/"+str(sample[1]))
        markup.add(inl_but)
    inline_Nazad = InlineKeyboardButton("Назад", callback_data='DOWN/'+str(sample[1]))
    inline_Vpered = InlineKeyboardButton("Вперед", callback_data='UP/'+str(sample[1]))
    markup.add(inline_Nazad,inline_Vpered)
    print(str(sample[1]))
    return markup
    


if __name__ == '__main__':
    k = ButtnUPDOWN(1)
    
