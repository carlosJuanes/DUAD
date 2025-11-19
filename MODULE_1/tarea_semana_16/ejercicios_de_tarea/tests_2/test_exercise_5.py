import pytest
from my_module_homework.exercise_5 import sort_alphabetically

def test_sort_alphabetically_normal_case():
    #Arrange
    original="car_sun_blue_rock_jazz_apple_table"
    expected="apple_blue_car_jazz_rock_sun_table"
    #Act
    result=sort_alphabetically(original)
    #Assert
    assert result==expected

def test_sort_alphabetically_empty_case():
    #Arrange
    original=""
    expected=""
    #Act
    result=sort_alphabetically(original)
    #Assert
    assert result==expected

def test_sort_alphabetically_with_numbers():
    #Arrange
    original="3_car_sun_10_blue_201_rock_jazz_1534_apple_table"
    expected="10_1534_201_3_apple_blue_car_jazz_rock_sun_table"
    #Act
    result=sort_alphabetically(original)
    #Assert
    assert result==expected