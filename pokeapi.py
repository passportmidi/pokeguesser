# https://realpython.com/api-integration-in-python/

import requests
import random

def get_random_pokemon():
    # there are 1025 pokemon species (at the time of writing)
    pokedex_number = random.randint(1, 1025) 
    api_url = f"https://pokeapi.co/api/v2/pokemon/{pokedex_number}"
    response = requests.get(api_url)
    return response.json()