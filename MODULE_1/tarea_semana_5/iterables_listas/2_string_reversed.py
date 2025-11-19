# Create a program that iterates and prints a string letter by letter from right to left.
phrase=("May the force be with you")
length=len(phrase)

for index in range(length-1,-1,-1):
    letter=phrase[index]
    print(letter)