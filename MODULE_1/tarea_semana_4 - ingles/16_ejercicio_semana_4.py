#Create an algorithm that asks the user for 100 numbers and displays the largest among them.

counter=1
total_numbers=100
largest_number=float(input(f" please enter  number  {counter} = "))

while counter<total_numbers:
    counter=counter+1
    current_number=float(input(f" please enter number {counter}= "))
    if current_number>largest_number:
        largest_number=current_number
print(f"the largest number is  {largest_number}")
