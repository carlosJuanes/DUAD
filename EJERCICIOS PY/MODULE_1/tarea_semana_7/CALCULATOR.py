
# Create a command-line calculator. It should have a current number and a menu to decide which operation to perform 
# with another number:
# Addition
# Subtraction
# Multiplication
# Division
# Clear result
# When selecting an option, the user must enter the new number to add, subtract, multiply, or divide by the current number. 
# The result should then become the new current number.
# You must display error messages if the user selects an invalid option or if they enter an invalid number when performing 
# an operation.

"""CALCULATOR"""

current_number = 0.0 
while True:
    print("---------------------")
    print("     CALCULATOR")
    print("---------------------")

    print(f"{current_number}") 
    print(f"What do you want to do:\n"
          f"1 = Add\n"
          f"2 = Subtract\n"
          f"3 = Multiply\n"
          f"4 = Divide\n"
          f"5 = Clear result\n"
          f"6 = Exit") 
    
    operation_input = input(f"Select an option: ")
    
    try:
        operation_num = int(operation_input)
        if operation_num<1 or operation_num>6:
            print("please enter a valid number")
        elif operation_num == 1:
            try:
                number_to_add = float(input(f"Enter the number to add {current_number}+ "))
                current_number += number_to_add
                print(f"={current_number}")
            except ValueError:
                print("¡Error! Please enter a valid number.")
        elif operation_num == 2:
            try:
                number_to_subtract = float(input(f"Enter the number to subtract {current_number}- "))
                current_number = current_number - number_to_subtract
                print(f"={current_number}")
            except ValueError:
                print("¡Error! Please enter a valid number.")
        elif operation_num == 3:
            try:
                number_to_multiply = float(input(f"Enter the number to multiply {current_number}* "))
                current_number = current_number * number_to_multiply
                print(f"={current_number}")
            except ValueError:
                print("¡Error! Please enter a valid number.")
        elif operation_num == 4:
            try:
                number_to_divide = float(input(f"Enter the number to divide {current_number}/ "))
                current_number = current_number / number_to_divide
                print(f"={current_number}")
            except ZeroDivisionError:
                print("¡Error! Cannot divide by zero.")
        elif operation_num == 5:
            current_number = 0.0
            print(f"{current_number}")
            print("result cleared") 
        elif operation_num == 6:
            print("Exiting the calculator.")
            break
        else:
            print("Invalid option, please enter a number from 1-6.")
    except ValueError:
        print("Please enter a valid value.")