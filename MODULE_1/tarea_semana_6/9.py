# 9. Create a function that accepts a list of words and a number n, and returns a new list with only the words that have more than n letters."
# "- Example:
# - words = ["cielo", "sol", "maravilloso", "día"]
# - n = 4
# - Result → ["cielo", "maravilloso"]"



def filter_words_by_length(word_list, n):
    new_word_list = []
    for word in word_list:
        if len(word) > n:
            new_word_list.append(word)
    return new_word_list

words_to_filter = ["cielo", "sol", "perro", "gato", "extraterrestre", "luz", "uno"]
n_value = 4 
found_words = filter_words_by_length(words_to_filter, n_value)
print(f"Original list: {words_to_filter}")
print(f"Words with more than {n_value} letters: {found_words}")