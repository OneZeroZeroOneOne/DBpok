import sqlite3
 
def main():
    conn = sqlite3.connect("PokemonDB.db")
    cursor = conn.cursor()
    imp = open('Pokemon.csv', 'r')
    t = 0
    for i in imp:
        if t > 0:
            k = i.split(',')
            k[1]=k[1].replace("'", "`")
            sql_command = "INSERT INTO PokemonDB(PokemonID, Name, TP, TPP, Totl, HP , Attack, Defense, SpAtk , SpDef, Speed, Generation, Legendary) VALUES({},'{}','{}','{}',{},{},{},{},{},{},{},{},'{}')".format(*k)
            print(sql_command)
            cursor.execute(sql_command)
            conn.commit()
        t = t + 1

if __name__ == "__main__":
    main()
