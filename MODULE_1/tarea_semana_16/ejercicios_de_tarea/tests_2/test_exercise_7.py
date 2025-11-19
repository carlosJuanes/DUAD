import pytest
from my_module_homework.exercise_7 import count_character_occurrences

def test_count_character_occurrences_normal_case():
    #Arrange
    text="programming"
    character="r"
    expected=2
    #Act
    result=count_character_occurrences(text, character)
    #Assert
    assert result==expected

def test_count_zero_occurrences():
    #Arrange
    text="programming"
    character="z"
    expected=0
    #Act
    result=count_character_occurrences(text, character)
    #Assert
    assert result==expected

def test_count_with_upper_case():
    #Arrange
    text="Programming with python"
    character="P"
    expected=1
    #Act
    result= count_character_occurrences(text, character)
    #Assert
    assert result==expected


    