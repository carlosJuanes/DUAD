#13 Create an algorithm that asks the user for 3 numbers. If one of those numbers is 30,
#  or if all three numbers sum up to 30, display "Correct".
# Otherwise, display "Incorrect".

total_sum=30
number_1=int(input("enter your first number: "))
number_2=int(input("enter your second number: "))
number_3=int(input("enter your third number: "))

if (number_1==30)or(number_2==30)or(number_3==30)or(number_1+number_2+number_3==total_sum):
    print("CORRECT")
else:
    print("INCORRECT")
