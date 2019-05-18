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
        inl_but = InlineKeyboardButton("{}".format(DBworker.DB.Sample(IdPokemon,i)[2]), callback_data = "ID/"+str(IdPokemon+i))
        markup.add(inl_but)
    inline_Nazad = InlineKeyboardButton("Назад", callback_data='NAZ/'+str(IdPokemon))
    inline_Vpered = InlineKeyboardButton("Вперед", callback_data='VPERED/'+str(IdPokemon))
    markup.add(inline_Nazad,inline_Vpered)
    print("klava robe")

    return markup

def CreatePaginationMarkup(start_from_id, db):
    poks = db.get_pokemon_list(start_from_id, settings.pokemons_per_page)
    markup = InlineKeyboardMarkup()
    for i in poks:
        inl_but = InlineKeyboardButton(i['Name'], callback_data = "ID/"+str(i['ID']))
        markup.add(inl_but)

    markup.row(InlineKeyboardButton("Назад", callback_data='NAZ/'+str(start_from_id-6)),
                InlineKeyboardButton("Вперед", callback_data='VPERED/'+str(start_from_id+6)))

    return markup

def CansBut(IdPokemon):
    if IdPokemon < 1:
        IdPokemon = 1
    if IdPokemon > 715:
        IdPokemon = 715
    markup = InlineKeyboardMarkup()
    inline_Сans = InlineKeyboardButton("Отмена", callback_data='CANS/'+str(IdPokemon))
    inline_NEXT = InlineKeyboardButton("Следующий", callback_data='NEXT/'+str(IdPokemon))
    inline_PRED = InlineKeyboardButton("Предыдущий", callback_data='PRED/'+str(IdPokemon))
    markup.row(inline_PRED,inline_NEXT)
    markup.add(inline_Сans)
    return markup



if __name__ == '__main__':
    k = ButtnUPDOWN(1)
