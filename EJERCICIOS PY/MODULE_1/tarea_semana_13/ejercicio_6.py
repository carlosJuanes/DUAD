"""Create a function named multiply, which takes two values and multiplies them.
This function should be combined with two decorators:
@log_call: prints the function's name, arguments, current date, and return value.
@validate_numbers: checks that all arguments are numeric."""
import datetime

def log_call(func):
    def wrapper(*args):
        result=func(*args)
        print(f"func:{func.__name__} - args: {args}, - {datetime.datetime.now()} - result {result}")
        return result
    return wrapper

def validate_numbers(func):
    def wrapper(*args, **kwarg):
        for arg in args:
            try:
                float(arg)
            except ValueError:
                raise TypeError("Error! Argument is not a number.")
        for value in kwarg.values():
            try:
                float(value)
            except ValueError:
                raise TypeError("Error! Argument is not a number.")        
        result=func(*args, **kwarg)
        return result
    wrapper.__name__ = func.__name__ 
    return wrapper

@log_call
@validate_numbers
def multiply(number_1, number_2):
    result=number_1*number_2
    return result

try:
    multiply(4, 5)
except TypeError as e:
    print(e)