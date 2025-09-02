# 3-. Create a program that opens a .csv file with video game information (the one generated in exercise 1) and:
# - Reads each line using `csv.reader()`
# - Displays the content on screen in a readable format, line by line
import csv
def file_reader(path):
    with open(path, "r", newline='') as file:
        reader=csv.reader(file)
        headers=next(reader)
        for row in reader:
            for key, value in zip(headers, row):
                print(f"{key}:{value}")
            print()

file_reader("videojuegos.csv")