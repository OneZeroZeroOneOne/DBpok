from schematics.models import Model
from schematics.types import StringType, DecimalType, BooleanType

class Pokemon(Model):
    DbID = DecimalType(required=True)
    ID = DecimalType(required=True)
    Name = StringType(required=True)
    Type1 = StringType()
    Type2 = StringType()
    Totl = StringType(required=True)
    HP = DecimalType(required=True)
    Defense = DecimalType(required=True)
    SpAtk = DecimalType(required=True)
    Speed = DecimalType(required=True)
    Generation = DecimalType(required=True)
    Legendary = BooleanType(required=True)

    EvolutionFrom = DecimalType()
    EvolutionInto = DecimalType()

    def __init__(self, arr_val):
        super(Pokemon, self).__init__()
        attrib = self.keys()
        for n, i in enumerate(arr_val):
            self[attrib[n]] = i

    def GetEvolutions(self):
        """
            володя тут добав шоб із бази витягувались еволюциї покемона
            взавісімості от його ІД
        """
        pass


#TEST
#мона не запускать
#Pokemon([1, 1, "name", "qwe1", "qwe2", 100, 100, 100, 100, 100, 100, True])
