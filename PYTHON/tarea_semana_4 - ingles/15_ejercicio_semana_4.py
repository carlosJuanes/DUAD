#15. Create an algorithm that asks the user for a number and displays:

#"Fizz" if it's divisible by 3.
#"Buzz" if it's divisible by 5.
#"FizzBuzz" if it's divisible by both

entered_number=float(input("please enter a number= "))
if (entered_number % 3==0)and(entered_number % 5 ==0 ):
    print("fizzbuzz")
elif entered_number % 3==0:
    print("fizz")
elif entered_number % 5 ==0:
    print("buzz")