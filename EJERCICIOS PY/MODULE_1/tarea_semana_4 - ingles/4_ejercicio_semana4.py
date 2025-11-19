#4. Create a program that asks the user for three numbers and then displays the largest among them.


first_number=int(input("enter your first number"))
second_number=int(input("enter your second number"))
third_number=int(input("enter your third number"))

largest_number=first_number
if second_number>first_number:
    largest_number=second_number
if third_number>largest_number:
    largest_number=third_number
print(f"the largest number is {largest_number}")
