import pytest
from my_module_homework.exercise_6 import get_prime_numbers

def test_get_prime_number_normal_case():
    #Arrange
    Original=[7,2,20,15,36,44,63,100,77,15,93,19,1]
    expected=[7,2,19]
    #Act
    result=get_prime_numbers(Original)
    #Assert
    assert result==expected

def test_get_prime_number_without_prime():
    #Arrange
    original=[20,15,36,44,63,100,77,15,93,1]
    expected=[]
    #Act
    result=get_prime_numbers(original)
    #Assert
    assert result==expected

def test_get_prime_number_with_string():
    #Arrange
    original="20,15,1.30,36,44,40.5,63,100,77,15,93,7.8,1"
    #Act, Assert
    with pytest.raises(TypeError):
        get_prime_numbers(original)


        