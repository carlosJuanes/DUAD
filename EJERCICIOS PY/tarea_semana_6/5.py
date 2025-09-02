# 5. Create a function that prints the number of uppercase and the number of lowercase letters in a string."
#   Example: 'I love Nación Sushi' → 'There’s 3 upper cases and 13 lower cases'"


def count_cases(text): 
    uppercase_count = 0
    lowercase_count = 0
    for char in text: 
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    print(f"The string has {uppercase_count} uppercase letters and {lowercase_count} lowercase letters.")

count_cases("I love Nation Sushi")