import requests
import sqlite3
import settings
from bs4 import BeautifulSoup
from lxml import html


url = "https://pokemondb.net/pokedex/national"
url_domain = "https://pokemondb.net"
where_to_save = "new_pokemons_img"
global_count = 1
conn = sqlite3.connect(settings.poke_db)
#self.conn.row_factory = dict_factory
cursor = conn.cursor()

def get_pokemons_page(url = url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    pokemon_list = soup.find_all('div', {"class":"infocard-list infocard-list-pkmn-lg"})
    pokemons_page = []
    for pokemons in pokemon_list:
        for pokemon in pokemons.find_all('div', {"class":"infocard "}):
            p_link = pokemon.find("a")
            #print(url_domain+p_link['href'])
            pokemons_page.append(url_domain+p_link['href'])

    return pokemons_page

def get_pokemon_images(url):
    global global_count
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    species_list = soup.find("div", {"class":"tabs-panel-list"})
    specie_id = soup.find("table", {"class":"vitals-table"}).find('tbody').find_all('tr')[0]
    specie_id = int(specie_id.find('td').text)
    img_links = []
    print(specie_id)
    #for i in specie_id:
    #    print(i, '\n')
    for specie in species_list:
        s = specie.find("img")#, {"class":"tabs-panel"})
        #print("img", s)
        if not isinstance(s, int):
            img_links.append(s['src'])

    print(img_links)
    for link in img_links:
        file_name = where_to_save + "\\" +str(global_count)+"#"+str(specie_id)+".jpg" #link.split("/")[-1]
        r = requests.get(link, stream=True)
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
        global_count+=1;

def save_pokemon_to_db(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    tree = html.fromstring(r.text)

    species_list = soup.find("div", {"class":"tabs-panel-list"})
    specie_id = soup.find("table", {"class":"vitals-table"}).find('tbody').find_all('tr')[0]
    specie_id = int(specie_id.find('td').text)
    img_links = []
    print(specie_id)
    #for i in specie_id:
    #    print(i, '\n')
    for specie in species_list:
        s = specie.find("img")#, {"class":"tabs-panel"})
        #print("img", s)
        if not isinstance(s, int):
            img_links.append(s['src'])

    print(img_links)

    '''pokedex_data = soup.find("div", {"tabset-basics tabs-wrapper tabs-onetab"})
    print(pokedex_data)
    new_d = pokedex_data.find("div", {"grid-col span-md-6 span-lg-4"})
    print(new_d)'''
    p_type = tree.xpath('//*[@id="tab-basic-1"]/div[1]/div[2]/table/tbody/tr[2]/td')[0]
    print(dir(p_type))
    print(p_type.text_content)

def get_parent(n, who, l):
    cur = l[n-1]
    return cur if cur<who else -1

def get_child(n, who, l):
    if n+1<len(l):
        return l[n+1]
    return -1

def get_neigh(who, l):
    for n, i in enumerate(l):
        if i == who:
            return [get_parent(n, who, l), get_child(n, who, l)]

def validate(l):
    if l[0]+1 == l[1]:
        return False
    return True

def get_pokemon_evolution(url):
    conn = sqlite3.connect("PokemonDB.sqlite") # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    specie_id = soup.find("table", {"class":"vitals-table"}).find('tbody').find_all('tr')[0]
    specie_id = int(specie_id.find('td').text)

    evo_list = soup.find("div", {"class":"infocard-list-evo"})
    if evo_list is not None:
        evo_list = evo_list.find_all("div", {"class", "infocard"})
        evo_list = [int(i.find('span', {"class":"infocard-lg-data text-muted"}).find('small').text.replace("#", "")) for i in evo_list]
        #for i in evo_list:
        #    cur_id =
        #    print(int(cur_id))
        neigh = get_neigh(specie_id, evo_list)
        if neigh:
            isvalid = validate(neigh)
            print(neigh, isvalid)
            if isvalid:
                try:
                    cursor.execute("INSERT INTO Evolution (ID, FromID, ToID) VALUES({}, {}, {})".format(specie_id, neigh[0], neigh[1]))
                except:
                    pass
            else:
                try:
                    cursor.execute("INSERT INTO Evolution (ID, FromID, ToID) VALUES({}, {}, {})".format(specie_id, -1, -1))
                except:
                    pass
        else:
            try:
                cursor.execute("INSERT INTO Evolution (ID, FromID, ToID) VALUES({}, {}, {})".format(specie_id, -1, -1))
            except:
                pass
    else:
        print("no evolutions with ", specie_id)
        try:
            cursor.execute("INSERT INTO Evolution (ID, FromID, ToID) VALUES({}, {}, {})".format(specie_id, -1, -1))
        except:
            pass
    conn.commit()

pokemon_list = get_pokemons_page(url = url)
#for i in pokemon_list:
    #get_pokemon_evolution(i)
#get_pokemon_evolution(pokemon_list[19])
#print(get_neigh(2, [1, 2, 3]))
#for i in pokemon_list:

print(save_pokemon_to_db("https://pokemondb.net/pokedex/bulbasaur"))
