# 10. Create a function that accepts a string and returns how many vowels it contains."
# "- Example:
# - phrase = Hola mundo
# - Result → 4"

def count_vowels(text):
    count = 0
    for char in text:
        if char.lower() in "aeiou":
            count += 1
    return count


my_text_string = "hola mundo" 
vowel_count = count_vowels(my_text_string) 
print(f"The word '{my_text_string}' contains {vowel_count} vowels.")