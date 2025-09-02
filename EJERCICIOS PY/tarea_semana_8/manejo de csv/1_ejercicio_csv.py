#1-  Create a program that allows me to enter information for 'n' video games and save it to a text file.


import csv

header=["name", "genre", "developer", "classification"]
def enter_video_games():
    video_games=[]
    while True:
        entered_video_games=input("Do you want to enter video games into the database? ")
        video_games_lowercase=entered_video_games.lower()
        if video_games_lowercase=="yes":
            name=input("Enter the name of the video game: ")
            genre=input("Enter the genre of the video game: ")
            developer=input("Enter the developer of the video game: ")
            classification=input("Enter the classification of the video game: ")
            current_video_game={
                "name":name,
                "genre":genre,
                "developer":developer,
                "classification":classification
            }
            video_games.append(current_video_game)
        elif video_games_lowercase=="no":
            break
        else:
            print("Invalid response. Please enter yes or no.")
    return video_games


def save_video_games(file_path, data, header):
    with open(file_path, "w",encoding="utf-8", newline="") as file:
        writer=csv.DictWriter(file,fieldnames=header)
        writer.writeheader()
        writer.writerows(data)


my_games=enter_video_games()
save_video_games("videojuegos.csv",my_games,header)