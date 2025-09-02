# - Create a program that:
# - Asks the user for a line of text
# - Adds that line **to the end** of an existing file
# - If the file does not exist, it creates it automatically


def add_text(path):
    with open(path,'a') as file:
        new_song=input("Enter a new song = ")
        file.write(new_song+'\n')
        print(new_song)
    print("Song successfully added to your song list!!!")
add_text("canciones.txt")
