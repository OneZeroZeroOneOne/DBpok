import requests
from bs4 import BeautifulSoup


url = "https://pokemondb.net/pokedex/national"
url_domain = "https://pokemondb.net"
where_to_save = "pokemons_img"

def get_pokemons_page(url):
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
        file_name = where_to_save + "\\" +str(specie_id)+"#"+ link.split("/")[-1]
        r = requests.get(link, stream=True)
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)


pokemon_list = get_pokemons_page(url)
for i in pokemon_list:
    get_pokemon_images(i)
