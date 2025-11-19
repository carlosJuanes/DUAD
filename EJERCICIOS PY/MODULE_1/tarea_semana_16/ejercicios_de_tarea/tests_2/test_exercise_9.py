import pytest
from my_module_homework.exercise_9 import count_vowels

def test_count_vowels_normal_case():
    #Arrange
    my_text_string="Programming with python"
    expected=5
    #Act
    result=count_vowels(my_text_string)
    #Assert
    assert result==expected

def test_count_vowel_empty_string():
     #Arrange
    my_text_string=""
    expected=0
    #Act
    result=count_vowels(my_text_string)
    #Assert
    assert result==expected

def test_count_vowel_with_numbers():
    #Arrange
    my_text_string=12345
    #Act, Assert
    with pytest.raises(TypeError):
        count_vowels(my_text_string)


        