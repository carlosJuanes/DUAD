# 5-Create a program that opens a .json file with Pokémon information (based on the JSON generated in exercise 1) and:
# Read the JSON file
# Group Pokémon by type (e.g., "water", "fire", etc.)
# Calculate and show the average level for each type:


import json

def load_pokemons(file_path):
    with open(file_path, "r") as file:
        python_data = json.load(file)
        return python_data
    
existing_pokemons = load_pokemons("pokemones.json")

levels_by_type = {}
def calculate_average(num_list):
    total_sum = sum(num_list)
    count = len(num_list)
    average = total_sum / count
    return average

for pokemon in existing_pokemons:
    pokemon_base = pokemon["base"]
    pokemon_level = calculate_average(pokemon_base.values())
    for pokemon_type in pokemon["type"]:
        if pokemon_type in levels_by_type:
            levels_by_type[pokemon_type].append(pokemon_level)
        else:
            levels_by_type[pokemon_type] = [pokemon_level]

for key, value in levels_by_type.items():
    type_average = calculate_average(value)
    print(f"Type {key} average level: {type_average:.2f}")