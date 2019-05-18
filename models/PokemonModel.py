from schematics.models import Model
from schematics.types import StringType, DecimalType, BooleanType
import os

pokemon_description = """*Имя покемона:* {}
*В общем:* {}
*Атака:* {}
*HP:* {}
*Защита:* {}
*Тип 1:* {}
*Тип 2:* {}
*Ск.Атк:* {}
*Cк.Защ:* {}
*Скорость:* {}
*Поколение:* {}
*Легендарность:* {}

*ID:* {}"""

class Pokemon(Model):
    ID = DecimalType(required=True)
    PokemonID = DecimalType(required=True)
    Name = StringType(required=True)
    TP = StringType()
    TPP = StringType()
    Totl = DecimalType(required=True)
    HP = DecimalType(required=True)
    Attack = DecimalType(required=True)
    Defense = DecimalType(required=True)
    SpAtk = DecimalType(required=True)
    SpDef = DecimalType(required=True)
    Speed = DecimalType(required=True)
    Generation = DecimalType(required=True)
    Legendary = BooleanType(required=True)

    Image = StringType()

    EvolutionFrom = DecimalType()
    EvolutionInto = DecimalType()

    def __init__(self, DbID, db):
        self.db = db
        self.DbID = DbID

        arr_val = self.db.get_pokemon_by_dbid(self.DbID)
        super(Pokemon, self).__init__(arr_val)

        self.GetImage()
        self.GetEvolutions()

    def GetImage(self):
        self.Image = "new_pokemons_img/{}#{}.jpg".format(self.ID, self.PokemonID)
        #print(self.Image)

    def validate(self):
        super(Pokemon, self).validate()
        exists = os.path.isfile(self.Image)
        if not exists:
            raise Exception("Image of Pokemon with ID {} doesnt exist :(".format(self.PokemonID))
        #print(self.items())


    def GetEvolutions(self):
        self.EvolutionFrom, self.EvolutionInto = self.db.get_evolutions_by_id(self.ID)

    def GetNextEvolution(self):
        if self.EvolutionInto != -1:
            return Pokemon(self.EvolutionInto, self.db)
        return None

    def GetPrevEvolution(self):
        if self.EvolutionFrom != -1:
            return Pokemon(self.EvolutionFrom, self.db)
        return None

    def ToString(self):
        return pokemon_description.format(self.Name, self.Totl, self.Attack,
        self.HP, self.Defense, self.TP,
        self.TPP, self.SpAtk, self.SpDef,
        self.Speed,
        self.Generation, self.Legendary, self.ID)
