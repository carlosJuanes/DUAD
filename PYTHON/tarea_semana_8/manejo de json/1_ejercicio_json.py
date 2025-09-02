#1-  Create a program that allows me to add a new Pokémon to the JSON file from the lesson.
# It should read the file to import the existing Pokémon, then ask for the new Pokémon's information,
# and finally save the new Pokémon to the file.




import json

def load_pokemon_data(file_path):
    with open(file_path, "r") as file:
        python_data = json.load(file)
        return python_data


def create_new_pokemon():
    name = input("Please enter the name of the new pokemon: ")
    name_dict = {"english": name}
    entered_type = input("Please enter the pokemon's type: ")
    type_list = [entered_type]
    print("Please enter the base information")
    base_hp = int(input("Please enter the HP: "))
    base_attack = int(input("Please enter the attack: "))
    base_defense = int(input("Please enter the defense: "))
    base_sp_attack = int(input("Please enter the sp attack: "))
    base_sp_defense = int(input("Please enter the sp defense: "))
    base_speed = int(input("Please enter the speed: "))
    base_dict = {
      "HP": base_hp,
      "Attack": base_attack,
      "Defense": base_defense,
      "Sp. Attack": base_sp_attack,
      "Sp. Defense": base_sp_defense,
      "Speed": base_speed
      }
    new_pokemon_data = {
        "name": name_dict,
        "type": type_list,
        "base": base_dict
    }
    return new_pokemon_data

existing_pokemon = load_pokemon_data("pokemones.json")
new_pokemon = create_new_pokemon()
existing_pokemon.append(new_pokemon)


with open("pokemones.json", "w") as file:
    json.dump(existing_pokemon, file, indent=4)

print("The new pokemon has been successfully added and the file has been saved")