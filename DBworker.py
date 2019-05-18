import sqlite3
import settings

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class DB:
    def __init__(self):
        self.conn = sqlite3.connect("{}".format(settings.poke_db))
        self.conn.row_factory = dict_factory
        self.cursor = self.conn.cursor()

    def get_pokemon_by_dbid(self, pok_id):
        sql_command = "SELECT * FROM PokemonDB WHERE ID = {}".format(pok_id)
        self.cursor.execute(sql_command)

        data = self.cursor.fetchone()
        data['Legendary'] = False if data['Legendary'][0] == 'F' else True

        return data

    def get_evolutions_by_id(self, pok_id):
        sql_command = "SELECT * FROM Evolution WHERE ID = {}".format(pok_id)
        self.cursor.execute(sql_command)

        data = self.cursor.fetchone()
        return [data['EvolutionFrom'], data['EvolutionInto']]


    def Sample(IdP,step):
        """
            GAVNO EBANOE
            NADO PEREDELAT'
        """
        conn = sqlite3.connect("{}".format(settings.poke_db))
        cursor = conn.cursor()
        sample = cursor.execute("SELECT * FROM PokemonDB WHERE PokemonID = {}".format(str(int(IdP)+step)))
        sample = cursor.fetchone()
        return sample

    def get_pokemon_list(self, pok_id, how_many):
        sql_command = "SELECT * FROM PokemonDB WHERE ID >= {} LIMIT {}".format(pok_id, how_many)
        self.cursor.execute(sql_command)

        data = self.cursor.fetchall()
        return data


#HOW TO USE IT!
#db = DB()
#print(db.get_pokemon_list(4, 6))
