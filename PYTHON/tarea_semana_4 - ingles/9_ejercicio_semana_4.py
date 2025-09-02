#9. Create an algorithm that asks the user for two numbers, 
# stores them in two distinct variables (first and second), 
# and then orders them from least to greatest within those same variables.

first_number=int(input(f"please enter your first number= "))
second_number=int(input(f"please your second number= "))

if first_number>second_number:
    print(f"{second_number} {first_number}")
else:
    print(f"{first_number} {second_number}")
    