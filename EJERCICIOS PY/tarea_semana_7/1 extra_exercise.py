# Create a program that:
# - Asks the user for their name
#     - If the name is numeric (isdigit()), raise ValueError("Name cannot be a number")
# - Then asks for their age
#     - If it's not a valid number, catch the ValueError and display a message
# If everything goes well, print a message: "Hello <name>, your age is <age>"

name = input("Please enter your name: ")

if name.isdigit():
    raise ValueError("Name cannot be a number")

while True:
    age = input("Please enter your age: ")
    try:
        age_int = int(age)
        print(f"Hello {name}, your age is {age_int}.")
        break
    except ValueError:
        print("Error! Invalid age.")