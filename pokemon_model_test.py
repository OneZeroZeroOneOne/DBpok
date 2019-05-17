from models.PokemonModel import Pokemon
from DBworker import DB

db = DB()

p = Pokemon(1, db)
p.validate()
next_evolution_pokemon = p.GetNextEvolution()
next_evolution_pokemon.validate()
print(p.ToString())
