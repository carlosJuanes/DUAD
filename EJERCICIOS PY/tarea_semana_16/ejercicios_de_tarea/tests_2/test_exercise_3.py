import pytest
from my_module_homework.exercise_3 import reverse_string

def test_reverse_string_success():
    #Arrange
    original="hello world"
    expected="dlrow olleh"
    #Act
    result=reverse_string(original)
    #Assert
    assert result==expected

def test_reverse_string_empty():
    #Arrange
    original=""
    expected=""
    #Act
    result=reverse_string(original)
    #Assert
    assert result==expected

def test_reverse_string_on_non_string():
    #Arrange
    original=123456789
    #Act, Assert
    with pytest.raises(TypeError):
        reverse_string(original)


        