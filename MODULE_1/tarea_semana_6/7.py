# 7. Create a function that accepts a list of numbers and returns a list containing only the prime numbers from it."
# "1. Example: [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]"
# "2. Tip 1: Research the mathematical logic to find out if a number is prime, and convert it to code. Don't look up the code; 
# that won't help."
# "3. Tip 2: Here you need to do several things (iterate through the list, check if each number is prime, 
# and add it to another list). So the best approach is to add another function to check if the number is prime or not."


def get_prime_numbers(numbers): 
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


my_list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 52, 36, 5, 748, 5, 4, 6, 2, 1, -4, -55, 7, 77, 7777, 4]
found_prime_numbers = get_prime_numbers(my_list_of_numbers)

print(f"Original list: {my_list_of_numbers}")
print(f"Found prime numbers: {found_prime_numbers}")