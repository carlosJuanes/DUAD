# - Create a program that:
# - Reads a file line by line
# - Converts each line to **uppercase**
# - Writes the content to a **new file**

def convert_to_uppercase(path):
    with open(path,'r') as file:
        with open("4_uppercase_songs.txt", 'w') as output_file:
            for line in file:
                uppercase_line=line.upper()
                output_file.write(uppercase_line)         
                print(uppercase_line)
        print("You have converted your song list to uppercase!!!")
convert_to_uppercase("canciones.txt")
