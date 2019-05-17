import settings
import DataBaseModule
from aiogram.types import ReplyKeyboardRemove, \
ReplyKeyboardMarkup, InlineKeyboardMarkup, \
InlineKeyboardButton
def ButtnUPDOWN(IdPokemon):
    markup = InlineKeyboardMarkup()
    weeklist = list()
    if IdPokemon < 1:
        IdPokemon = 1
    for i in range(0,6,1):
        inl_but = InlineKeyboardButton("{}".format(DataBaseModule.Sample(IdPokemon,i)[2]), callback_data = "ID/"+str(DataBaseModule.Sample(IdPokemon,i)[1]))
        markup.add(inl_but)
    inline_Nazad = InlineKeyboardButton("Назад", callback_data='NAZ/'+str(sample[1]))
    inline_Vpered = InlineKeyboardButton("Вперед", callback_data='NEXT/'+str(sample[1]))
    markup.add(inline_Nazad,inline_Vpered)
    return markup
    


if __name__ == '__main__':
    k = ButtnUPDOWN(1)
    
