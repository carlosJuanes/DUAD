# Create a program that reads song names from a file (line by line)
# and saves the same names, sorted alphabetically, into another file.


def sort_and_save_songs(path):
    clean_lines=[]
    with open(path, 'r') as file:
        for line in file:
            line_without_space=line.strip()
            clean_lines.append(line_without_space)
    clean_lines.sort()
    print(clean_lines)

    with open("1_sorted_songs.txt", 'w') as songs:
        for song in clean_lines:
            songs.write(song+"\n")
    print("You have alphabetically sorted your song list!!!")
sort_and_save_songs("canciones.txt")
