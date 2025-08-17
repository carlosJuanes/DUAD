# Create a program that reads a file with text line by line, removes newlines (\n)
# and writes all content into a single line in a new file


def read_and_join_lines(path):
    with open(path, 'r') as file:
        text_content=" "
        for line in file.readlines():
            line_without_hyphens=line.strip()
            text_content+=line_without_hyphens+" "
        print(text_content)
    with open("2_song_string.txt", "w") as text_output:
        text_output.write(text_content)
        print("You have copied your songs into a single line!!!")

read_and_join_lines("canciones.txt")
