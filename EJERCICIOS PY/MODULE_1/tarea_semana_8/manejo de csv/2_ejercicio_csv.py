# Read about the other methods of the csv module here and create an alternative version of the exercise
#  above that saves the file separated by tabs instead of commas.

import csv

def ask_for_data():
    game_name=input("Please enter the name of the video game: ")
    game_genre=input("Please enter the genre of the video game: ")
    game_developer=input("Please enter the developer of the video game: ")
    game_classification=input("Please enter the classification of the video game: ")
    current_game={
        "name":game_name,
        "genre":game_genre,
        "developer":game_developer,
        "classification":game_classification
    }
    return current_game


def collect_video_games():
    video_game_data=[]
    while True:
        enter_data=input("Do you want to enter video games into the database? ")
        data_lowercase=enter_data.lower()
        if data_lowercase=="yes":
            new_video_game=ask_for_data()
            video_game_data.append(new_video_game)
        elif data_lowercase=="no":
            break
        else:
            print("Invalid entry, please enter yes or no.")
    return video_game_data

keys=["name", "genre", "developer", "classification"]
def save_to_csv(file_path, data_list, header):
    with open(file_path, "w", encoding='utf-8') as file:
        writer=csv.DictWriter(file, header, delimiter="\t")
        writer.writeheader()
        writer.writerows(data_list)

save_to_csv("videojuegos.csv", collect_video_games(), keys)
