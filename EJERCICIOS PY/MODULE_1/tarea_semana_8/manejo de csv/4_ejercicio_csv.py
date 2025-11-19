# 4- Create a program that opens a .csv file with video game information
# (based on the CSV generated in exercise 1) and:
# - Reads the video game CSV file
# - Asks the user for an ESRB rating (for example: "T")
# - Displays all video games that have that rating

import csv

def find_video_games_by_rating(file_path):
    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        desired_rating = input("Enter the ESRB rating you are looking for: ")
        rating_uppercase = desired_rating.upper()
        found_game = False
        for row in reader:
            if rating_uppercase == row["rating"].upper():
                found_game = True
                for key, value in row.items():
                    print(f"{key}:{value}")
                print()
        if not found_game:
            print(f"No video games were found with the rating {desired_rating}.")

find_video_games_by_rating("videojuegos.csv")