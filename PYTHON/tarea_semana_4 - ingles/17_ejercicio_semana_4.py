#16. Create an algorithm that asks the user for 100 numbers and displays their sum.

counter=1
total_nm=5
sum_number=0

while counter<=total_nm:
    input_number=float(input(f"please enter the number {counter}= "))
    counter+=1
    sum_number+=input_number
print(f"the total of sum is {sum_number}")
