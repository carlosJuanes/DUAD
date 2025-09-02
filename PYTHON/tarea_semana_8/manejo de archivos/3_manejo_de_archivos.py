# Create a program that opens a text file and counts how many words it contains in total.

# (Consider that words are separated by spaces and/or newlines)


def count_words(path):
    with open(path,'r') as file:
        full_text=file.read()
        text_list=full_text.split()
        amount=len(text_list)
        print(f"This file contains {amount} words")

count_words("canciones.txt")