import sqlite3
import settings
def Sample(IdP,step):
    conn = sqlite3.connect("{}".format(settings.poke_db))
    cursor = conn.cursor()
    sample = cursor.execute("SELECT * FROM PokemonDB WHERE PokemonID = {}".format(str(IdP+step)))
    sample = cursor.fetchone()
    return sample
