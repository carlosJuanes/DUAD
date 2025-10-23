import pytest
import random
from my_module_homework.exercise_1 import my_bubble_sort

def test_sort_with_small_list():
    #Arrange
    unsort_list=[5,2,1,4,6,7,8,9,3]
    expected_list=[1,2,3,4,5,6,7,8,9]
    #Act
    result=my_bubble_sort(unsort_list)
    #Assert
    assert result==expected_list

def test_sort_with_large_list():
    #Arrange
    unsorted_list=[random.randint(1,1000) for _ in range(150)]
    expected_list=sorted(unsorted_list)
    #Act
    result=my_bubble_sort(unsorted_list)
    #Assert
    assert result==expected_list

def test_sort_with_empty_list():
    #Arrange
    unsorted_list=[]
    expected_list=[]
    #Act
    result=my_bubble_sort(unsorted_list)
    #Assert
    assert result==expected_list

def test_raise_error_on_non_list_parameter():
    #Arrange
    invalid_input=12345678910
    #Act, Assert
    with pytest.raises(TypeError):
        my_bubble_sort(invalid_input)


        