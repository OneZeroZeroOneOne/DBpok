from models.PokemonModel import Pokemon
from DBworker import DB

db = DB()

p = Pokemon(1, db)
p.validate()
print(p.TP, p.TPP)
