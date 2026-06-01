
# Making API requests

import requests
# You have to install requests module

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = base_url + "pokemon/"+name
    response = requests.get(url)

    if response.status_code == 200:
        print("Data retrieved Successfully")
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"failed to retrieve data from {url}. \n{response.status_code}")
        return None
    # < Response[200] > - This is what response is - a http status code of 200
pokemon_name = "typhlosion"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Pokemon name: {pokemon_info['name'].capitalize()}")
    print(f"Pokemon id: {pokemon_info['id']}")
    print(f"Pokemon height: {pokemon_info['height']}")
    print(f"Pokemon weight: {pokemon_info['weight']}")