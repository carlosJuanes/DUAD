# 4 Create a function that reverses a string and returns it."
# "1. We already did this in iterables."
# "2. Example: 'Hola mundo' → 'odnum aloH'"

def reverse_string(text): 
    reversed_text = ""
    for index in range(len(text) - 1, -1, -1):
        letter = text[index]
        reversed_text += letter
    return reversed_text


my_word = "hola mundo"
reversed_word = reverse_string(my_word) 
print(f"Original word: {my_word}, reversed word: {reversed_word}")