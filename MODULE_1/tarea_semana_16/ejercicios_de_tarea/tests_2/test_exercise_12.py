import pytest
from unittest import mock
from my_module_homework.exercise_12 import read_lines

def test_read_lines_raises_file_not_found():
    #Arrange
    non_existent_path = "false_route.xyz"
    #Act, Assert
    with pytest.raises(FileNotFoundError):
        read_lines(non_existent_path)

@mock.patch('builtins.open', new_callable=mock.mock_open, read_data="line 1\nline 2\n")
def test_read_lines_returns_mocked_content(mock_file):
    #Arrange
    expected_lines=["line 1\n", "line 2\n"]
    #Act
    result= read_lines("non_existent_route.txt")
    #Assert
    assert result==expected_lines



    