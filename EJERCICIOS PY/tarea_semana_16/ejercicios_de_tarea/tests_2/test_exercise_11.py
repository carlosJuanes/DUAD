import pytest
from my_module_homework.exercise_11 import divide

def test_divide_with_normal_case():
    #Arrange
    a=10
    b=2
    expected=5.0
    #Act
    result=divide(a, b)
    #Assert
    assert result==expected

def test_divide_by_zero():
    #Arrange
    a=10
    b=0
    #Act, Assert
    with pytest.raises(ValueError):
        divide(a, b)
    

def test_divide_with_string():
    #Arrange
    a=10
    b="abc"
    #Act, Assert
    with pytest.raises(TypeError):
        divide(a, b)



        