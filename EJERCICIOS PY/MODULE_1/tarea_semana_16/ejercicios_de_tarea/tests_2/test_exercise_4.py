import pytest
from my_module_homework.exercise_4 import count_cases

def test_count_cases_normal():
    #Arrange
    original="Hello World"
    expected="The string has 2 uppercase letters and 8 lowercase letters."
    #act
    result=count_cases(original)
    #Assert
    assert result==expected

def test_count_cases_empty_string():
    #Arrange
    original=""
    expected="The string has 0 uppercase letters and 0 lowercase letters."
    #Act
    result=count_cases(original)
    #Assert
    assert result==expected

def test_count_cases_on_not_string():
    #Arrange
    original=123456789
    #Act, Assert
    with pytest.raises(TypeError):
        count_cases(original)


        