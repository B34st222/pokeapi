import requests
import json
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
        # print(f"Pokemon name: {data['name']}")
        # print(f"Pokemon id: {data['id']}")
        # print(f"Pokemon height: {data['height']}")
        # print(f"Pokemon weight: {data['weight']}")
        # print(f"Pokemon abilities: {data['abilities']}")
    else:
        print("Pokemon not found")


pokemon_name = "raticate"
get_pokemon_info(pokemon_name)