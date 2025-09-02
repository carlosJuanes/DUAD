#14 Create an algorithm that asks the user for 5 numbers and then displays the largest among them.

first_number=float(input("enter the first number= "))
largest_number=first_number

second_number=float(input("enter the second number= "))
if second_number>largest_number:
    largest_number=second_number

third_number=float(input("enter the third number"))
if third_number>largest_number:
    largest_number=third_number

fourth_number=float(input("enter the fourth number"))
if fourth_number>largest_number:
    largest_number=fourth_number

fifth_number=float(input("enter the fifth number= "))
if fifth_number>largest_number:
    largest_number=fifth_number

print(f" the largest number is  {largest_number}")
