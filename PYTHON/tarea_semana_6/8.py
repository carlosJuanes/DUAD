# 8. Create a function that accepts a text string and a character, and returns how many times that character appears in the text."
# "- Example:
# - text = 'programacion'
# - character = 'o'
# - Result → 2"

def count_character_occurrences(text_string, char_to_find): 
    count = 0
    for char in text_string: 
        if char == char_to_find:
            count += 1
    return count


my_text = "programacion"
my_character = "o"
total_occurrences = count_character_occurrences(my_text, my_character) 
print(f"The character '{my_character}' appears {total_occurrences} times in '{my_text}'.")