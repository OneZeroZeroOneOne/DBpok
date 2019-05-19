import pokepy

BD = pokepy.V2Client()
pok = BD.get_pokemon(14)
print(dir(pok))
print(pok.get_url)
print(pok.get_stat())
