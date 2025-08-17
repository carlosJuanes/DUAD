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


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return None


def multiply(num1, num2):
    return num1 * num2


def get_valid_option():
    while True:
        option = input("Please select an option = ")
        try:
            option_int = int(option)
            if option_int < 1 or option_int > 6:
                print("Error! Please select a valid option from 1-6")
            else:
                return option_int
        except ValueError:
            print("Error! Please enter a valid option")


def display_menu():
    print(f"What do you want to do?:\n"
          f"1 = Add\n"
          f"2 = Subtract\n"
          f"3 = Multiply\n"
          f"4 = Divide\n"
          f"5 = Clear result\n"
          f"6 = Exit")


def get_second_number():
    while True:
        valid_number = input("Please enter a number = ")
        try:
            second_number = float(valid_number)
            return second_number
        except ValueError:
            print("Error! That is not a valid number. Try again.")


def run_calculator():
    current_number = 0.0
    while True:
        print("---------------------")
        print("     CALCULATOR")
        print("---------------------")
        display_menu()
        print(current_number)
        selection = get_valid_option()
        if selection == 1:
            number_to_add = get_second_number()
            result = add(current_number, number_to_add)
            current_number = result
        elif selection == 2:
            number_to_subtract = get_second_number()
            result = subtract(current_number, number_to_subtract)
            current_number = result
        elif selection == 3:
            number_to_multiply = get_second_number()
            result = multiply(current_number, number_to_multiply)
            current_number = result
        elif selection == 4:
            number_to_divide = get_second_number()
            result = divide(current_number, number_to_divide)
            if result is None:
                print("Error! Cannot divide by zero.")
            else:
                current_number = result
        elif selection == 5:
            current_number = 0.0
        elif selection == 6:
            print("--------------------")
            print("Closing program...")
            print("Goodbye.")
            print("--------------------")
            break


run_calculator()