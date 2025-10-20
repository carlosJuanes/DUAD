# 6. Create a function that accepts a string with words separated by hyphens and returns an identical string but sorted alphabetically."
# "1. You need to convert it to a list, sort it, and convert it back to a string."
# "2. Example: 'python-variable-funcion-computadora-monitor' → 'computadora-funcion-monitor-python-variable'"


def sort_alphabetically(hyphenated_string): 
    list_of_words = hyphenated_string.split("_")
    list_of_words.sort()
    sorted_string = "_".join(list_of_words)
    return sorted_string


my_hyphenated_string = "may_the_force_be_with_you" 
alphabetically_sorted_string = sort_alphabetically(my_hyphenated_string) 
print(f"String with hyphens: {my_hyphenated_string}")
print(f"Alphabetically sorted string: {alphabetically_sorted_string}")


