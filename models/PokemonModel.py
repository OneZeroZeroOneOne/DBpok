from schematics.models import Model
from schematics.types import StringType, DecimalType, BooleanType
import os


class Pokemon(Model):
    DbID = DecimalType(required=True)
    ID = DecimalType(required=True)
    Name = StringType(required=True)
    Type1 = StringType()
    Type2 = StringType()
    Totl = DecimalType(required=True)
    HP = DecimalType(required=True)
    Defense = DecimalType(required=True)
    SpAtk = DecimalType(required=True)
    Speed = DecimalType(required=True)
    Generation = DecimalType(required=True)
    Legendary = BooleanType(required=True)

    Image = StringType()

    EvolutionFrom = DecimalType()
    EvolutionInto = DecimalType()

    def __init__(self, arr_val):
        super(Pokemon, self).__init__()
        attrib = self.keys()
        for n, i in enumerate(arr_val):
            self[attrib[n]] = i
        self.GetImage()
        self.GetEvolutions()

    def GetImage(self):
        self.Image = "pokemons_img/{}#{}.jpg".format(self.ID, self.Name.replace("``", "").lower())
        exists = os.path.isfile(self.Image)
        #print(exists)


    def GetEvolutions(self):
        """
            володя тут добав шоб із бази витягувались еволюциї покемона
            взавісімості от його ІД
        """
        pass
