# 7. Create a function that accepts a list of numbers and returns a list containing only the prime numbers from it."
# "1. Example: [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]"
# "2. Tip 1: Research the mathematical logic to find out if a number is prime, and convert it to code. Don't look up the code; 
# that won't help."
# "3. Tip 2: Here you need to do several things (iterate through the list, check if each number is prime, 
# and add it to another list). So the best approach is to add another function to check if the number is prime or not."


def get_prime_numbers(numbers): 
    if not isinstance(numbers, list):
        raise TypeError("error, input must be a list")
    prime_numbers = []
    for number in numbers:
        if number <= 1:
            continue
        is_prime = True
        for index in range(2, number):
            if number % index == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(number)
    return prime_numbers



