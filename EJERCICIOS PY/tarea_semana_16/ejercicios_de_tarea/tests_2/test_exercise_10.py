import pytest
from my_module_homework.exercise_10 import MathOperations

def test_operation_sum_with_positive():
    #Arrange
    calculator=MathOperations()
    a=10
    b=5
    expected=15
    #Act
    result=calculator.sum(a, b)
    #Assert
    assert result==expected

def test_operation_sum_with_negative():
    #Arrange
    calculator=MathOperations()
    a=-10
    b=5
    expected=-5
    #Act
    result=calculator.sum(a, b)
    #Assert
    assert result==expected

def test_operation_sum_with_zero():
    #Arrange
    calculator=MathOperations()
    a=0
    b=5
    expected=5
    #Act
    result=calculator.sum(a, b)
    #Assert
    assert result==expected
"-----------------------------------------------------------------------------------------------------"

def test_operation_subtraction_with_positives():
    #Arrange
    calculator=MathOperations()
    a=10
    b=5
    expected=5
    #Act
    result=calculator.rest(a, b)
    #Assert
    assert result==expected

def test_operation_subtraction_with_negatives_numbers():
    #Arrange
    calculator=MathOperations()
    a=-10
    b=5
    expected=-15
    #Act
    result=calculator.rest(a, b)
    #Assert
    assert result==expected

def test_operation_subtraction_with_zero():
    #Arrange
    calculator=MathOperations()
    a=0
    b=5
    expected=-5
    #Act
    result=calculator.rest(a, b)
    #Assert
    assert result==expected

"-----------------------------------------------------------------------------------------------------"

def test_operation_division_with_positives_numbers():
    #Arrange
    calculator=MathOperations()
    a=10
    b=5
    expected=2
    #Act
    result=calculator.division(a, b)
    #Assert
    assert result==expected

def test_operation_division_with_negatives_numbers():
    #Arrange
    calculator=MathOperations()
    a=10
    b=-5
    expected=-2
    #Act
    result=calculator.division(a, b)
    #Assert
    assert result==expected

def test_operation_division_with_zero():
    #Arrange
    calculator=MathOperations()
    a=10
    b=0
    #Act, Assert
    with pytest.raises(ValueError):
        calculator.division(a, b)

        