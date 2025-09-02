# Create a program that opens a .json file with Pokémon information (based on the JSON generated in exercise 1) and:
# Read the Pokémon JSON file
# For each Pokémon, show its main stats (for example: attack, defense, speed, etc.)


import json

def load_pokemons(file_path):
    with open(file_path, "r") as file:
        python_data = json.load(file)
        return python_data

existing_pokemons = load_pokemons("pokemones.json")

for pokemon in existing_pokemons:
    print(f' Name: {pokemon["name"]["english"]}')
    print(f'Attack: {pokemon["base"]["Attack"]}')
    print(f' Defense: {pokemon["base"]["Defense"]}')
    print(f' Speed: {pokemon["base"]["Speed"]}')