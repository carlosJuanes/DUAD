# 3. Create a function that returns the sum of all numbers in a list."
#   "1. The function will have one parameter (the list) and return a number (the sum of all its elements)."
#   "2. Example: [4, 6, 2, 29] → 41"


def sum_numbers(numbers):
    total_sum = 0
    for n in numbers:
        total_sum += n
    return total_sum
