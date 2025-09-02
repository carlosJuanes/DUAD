# 6- Create a program that opens a .csv file with video game information
# (based on the CSV that was generated in exercise 1) and:
# Reads the video game .csv file
# Asks the user to enter a developer's name (e.g., "Ubisoft")
# Displays all video games developed by that company in a readable format:
import csv

def find_video_games_by_developer(file_path):
    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        developer_name = input("Please, enter the name of the developer: ")
        developer_lowercase = developer_name.lower()
        found_game = False
        found_games = []
        for row in reader:
            if row["developer"].lower() == developer_lowercase:
                found_game = True
                found_games.append(row)
        
        if found_game:
            print(f"Video games developed by {developer_name}:")
            for game in found_games:
                print(f"- {game['name']} (Rating: {game['rating']}, Genre: {game['genre']})")
        else:
            print(f"No video games from the developer {developer_name} were found.")

find_video_games_by_developer("videojuegos.csv")