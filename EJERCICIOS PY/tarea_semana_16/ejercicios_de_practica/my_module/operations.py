import numbers
def subtract(a, b):
    return a- b

def subtraction_without_negatives(a, b):
    if b>a:
        raise ValueError("The second number cannot be greater than the first in this operation")
    return a-b

def reverse_string(s):
    if not isinstance(s, str):
        raise TypeError("the input must be a text string")
    return s[::-1]

def is_even(number):
    if not isinstance(number, int):
        raise ValueError("the input must be an integer")
    return number%2==0