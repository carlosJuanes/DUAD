#3-  Create a program that opens a .json file with Pokémon information (based on the JSON generated in exercise 1) and:
# Read the Pokémon JSON file
# Ask the user for a Pokémon type
# Show all Pokémon of that type


import json

def load_pokemons(file_path):
    with open(file_path, "r") as file:
        python_data = json.load(file)
        return python_data

existing_pokemons = load_pokemons("pokemones.json")

search_type = input("Enter the Pokémon type you want to search for (water, electric, fire, etc):")
lowercase_type = search_type.lower()
found_pokemons = []

for pokemon in existing_pokemons:
    pokemon_types = [pokemon_type.lower() for pokemon_type in pokemon["type"]]
    if lowercase_type in pokemon_types:
        found_pokemons.append(pokemon["name"]["english"])

if found_pokemons:
    print("The Pokémon that exist of that type are:")
    for name in found_pokemons:
        print(name)
else:
    print(f"No Pokémon of the type '{search_type}' were found.")