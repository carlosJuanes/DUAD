import pytest
from my_module.operations import subtract, subtraction_without_negatives, reverse_string, is_even


def test_two_numbers():
    #Arrange
    num1=10
    num2=4
    #Act
    result= subtract(num1,num2)
    #Assert
    assert result==6


def test_raise_error_if_result_is_negative():
    #Arrange
    num1=4
    num2=10
    #Act, Assert
    with pytest.raises(ValueError):
        subtraction_without_negatives(num1, num2)

def test_reverse_string_success():
    #Arrange
    original="python"
    expected="nohtyp"
    #Act
    result=reverse_string(original)
    #Assert
    assert result==expected

def test_reverse_string_empty():
    #Arrange
    original=""
    expected=""
    #Act
    result= reverse_string(original)
    #Assert
    
def test_reverse_string_on_non_string():
    #Arrange
    invalid_input=12345
    #Act, Assert
    with pytest.raises(TypeError):
        reverse_string(invalid_input)

def test_is_even_with_even_number():
    #Arrange
    num=42
    #Act
    result=is_even(num)
    #Assert
    assert result is True

def test_is_even_with_odd_number():
    #Arrange
    num=15
    #Act
    result=is_even(num)
    #Assert
    assert result is False

def test_is_even_raises_error_on_non_int():
    #Arrange
    num=5.5
    #Act, Assert
    with pytest.raises(ValueError):
        is_even(num)


        