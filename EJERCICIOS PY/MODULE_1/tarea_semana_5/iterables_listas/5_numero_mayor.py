# Create a program that asks the user for 10 numbers, and at the end shows all the numbers they entered, followed by the highest number entered.

entered_numbers = []

for index in range(10):
    number = float(input(f"Please enter number {index + 1} of 10: "))
    entered_numbers.append(number)

highest_number = entered_numbers[0]

for n in entered_numbers:
    if n > highest_number:
        highest_number = n

print(f"Your entered numbers are = {entered_numbers}")
print(f"The highest number was: {highest_number}")