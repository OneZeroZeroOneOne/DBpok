
from aiogram.types import ReplyKeyboardRemove, \
ReplyKeyboardMarkup, InlineKeyboardMarkup, \
InlineKeyboardButton
def ButtnUPDOWN(NamePokemon,IdPokemon):
    markup1 = InlineKeyboardMarkup();
    inline_month = InlineKeyboardButton('год:'+str(year)+' месяц:' + str(month), callback_data='button1')
    markup1.add(inline_month)
    for i in range(0,6,1)
        weeklist = list()
        weeklist.append(InlineKeyboardButton(NamePokemon, callback_data = NamePokemon + IdPokemon )
    markup1.row(*weeklist)
    inline_Nazas = InlineKeyboardButton("Назад", callback_data='UP')
    inline_Vpered = InlineKeyboardButton("Вперед", callback_data='DOWN')
    markup1.add(inline_Nazad,inline_Vpered)
    return markup1
    
