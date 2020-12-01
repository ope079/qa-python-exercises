import pytest
from applications import list_of_squares

def test_list_of_squares_six():
    assert list_of_squares.list_of_squares(6) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

def test_list_of_squares_two():
    assert list_of_squares.list_of_squares(2) == {1: 1, 2: 4}

def test_list_of_squares_nine():
    assert list_of_squares.list_of_squares(9) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}