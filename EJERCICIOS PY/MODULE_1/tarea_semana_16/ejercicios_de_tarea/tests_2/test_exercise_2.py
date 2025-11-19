import pytest
from my_module_homework.exercise_2 import sum_numbers

def test_sum_positive_numbers():
    #Arrange
    numbers=[1,10,9,7,3]
    expected=30
    #Act
    result=sum_numbers(numbers)
    #Assert
    assert result==expected

def test_sum_with_negative_numbers():
    #Arrange
    numbers=[1,9,3,7,-10]
    expected=10
    #Act
    result=sum_numbers(numbers)
    #Assert
    assert result==expected

def test_sum_with_empty_list():
    #Arrange
    numbers=[]
    expected=0
    #Act
    result=sum_numbers(numbers)
    #Assert
    assert result==expected


