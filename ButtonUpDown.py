import settings
import DBworker
from aiogram.types import ReplyKeyboardRemove, \
ReplyKeyboardMarkup, InlineKeyboardMarkup, \
InlineKeyboardButton
def ButtnUPDOWN(IdPokemon):
    markup = InlineKeyboardMarkup()
    weeklist = list()
    if IdPokemon < 1:
        IdPokemon = 1
    if IdPokemon > 715:
        IdPokemon = 715
    for i in range(0,6,1):
        inl_but = InlineKeyboardButton("{}".format(DBworker.DB.Sample(IdPokemon,i)[2]), callback_data = "ID/"+str(DBworker.DB.Sample(IdPokemon,i)[1]))
        markup.add(inl_but)
    inline_Nazad = InlineKeyboardButton("Назад", callback_data='NAZ/'+str(DBworker.DB.Sample(IdPokemon,i)[1]))
    inline_Vpered = InlineKeyboardButton("Вперед", callback_data='NEXT/'+str(DBworker.DB.Sample(IdPokemon,i)[1]))
    markup.add(inline_Nazad,inline_Vpered)
    
    return markup
    
def CansBut(IdPokemon):
    markup = InlineKeyboardMarkup()
    inline_Сans = InlineKeyboardButton("Отмена", callback_data='CANS/'+str(DBworker.DB.Sample(IdPokemon,0)[1]))  
    markup.add(inline_Сans)
    return markup
    
    
    
if __name__ == '__main__':
    k = ButtnUPDOWN(1)
