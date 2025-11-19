#5-  Create a program that opens a .csv file with video game information
# (based on the CSV that was generated in exercise 1) and:
# Reads the video game .csv file
# Counts how many video games there are of each genre
# Displays the result in an organized way

import csv

def count_genres(file_path):
    genre_counter = {}
    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            current_genre = row["genre"] 
            if current_genre in genre_counter:
                genre_counter[current_genre] += 1
            else:
                genre_counter[current_genre] = 1
    
    sorted_genres = sorted(genre_counter.keys())
    print("Genres found")
    for genre in sorted_genres:
        count = genre_counter[genre]
        print(f"{genre}:{count}")

count_genres("videojuegos.csv")