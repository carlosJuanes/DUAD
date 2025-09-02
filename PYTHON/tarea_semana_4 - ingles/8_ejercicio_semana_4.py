#8. Create an algorithm that asks the user for a number, and then calculates the sum of every number from 1 up to that entered number.

#Finally, display the result of the sum.

counter=1
total_sum=0
entered_number=int(input(f"please enter your number= "))
while counter<=entered_number:
    total_sum+=counter
    counter+=1
print(f" the result is = {total_sum}")