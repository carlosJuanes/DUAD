from my_module_homework.exercise_8 import filter_words_by_length

def test_filter_words_by_length_normal_case():
    #Arrange
    words_to_filter = ["apple", "orange", "banana", "lemon", "grape", "watermelon","pineapple", "mango"]
    n_value = 6
    expected=["watermelon", "pineapple"]
    #Act
    result=filter_words_by_length(words_to_filter, n_value)
    #Assert
    assert result==expected

def test_filter_words_empty_list():
    #Arrange
    words_to_filter=[]
    n_value=4
    expected=[]
    #Act
    result=filter_words_by_length(words_to_filter, n_value)
    #Assert
    assert result==expected

def test_filter_words_no_matches():
    #Arrange
    words_to_filter = ["apple", "orange", "banana", "lemon", "grape", "watermelon","pineapple", "mango"]
    n_value = 10
    expected=[]
    #Act
    result=filter_words_by_length(words_to_filter, n_value)
    #Assert
    assert result==expected


    