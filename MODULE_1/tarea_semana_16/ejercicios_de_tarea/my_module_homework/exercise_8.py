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


