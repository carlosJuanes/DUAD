# 4 Create a function that reverses a string and returns it."
# "1. We already did this in iterables."
# "2. Example: 'Hola mundo' → 'odnum aloH'"

def reverse_string(text): 
    if not isinstance(text, str):
        raise TypeError("the input must be a text string")
    reversed_text = ""
    for index in range(len(text) - 1, -1, -1):
        letter = text[index]
        reversed_text += letter
    return reversed_text

