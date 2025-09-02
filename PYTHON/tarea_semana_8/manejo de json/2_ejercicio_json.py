# 2- Create a program that opens a .json file with Pokémon information 
# (based on the JSON that was generated in exercise 1) and:
# Reads the JSON file of Pokémon
# Iterates through the list of Pokémon and displays their name, type, and level 
# (or any other defined attribute) in the console.

import json

def load_pokemon_data(file_path):
    with open(file_path, "r") as file:
        python_data = json.load(file)
        return python_data

existing_pokemon = load_pokemon_data("pokemones.json")

for pokemon in existing_pokemon:
    print(f'Name= {pokemon["name"]["english"]}')
    print(f'Type= {pokemon["type"]}')
    print("Bases")
    print(f'HP= {pokemon["base"]["HP"]}')
    print(f'Attack= {pokemon["base"]["Attack"]}')
    print(f'Defense= {pokemon["base"]["Defense"]}')
    print(f'Sp. Attack= {pokemon["base"]["Sp. Attack"]}')
    print(f'Sp. Defense= {pokemon["base"]["Sp. Defense"]}')
    print(f'Speed= {pokemon["base"]["Speed"]}')