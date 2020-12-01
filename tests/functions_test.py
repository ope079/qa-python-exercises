import pytest
from exercises import functions

def test_F():
    assert functions.grades("Frank", 17, 46, 80) == "Frank scored 82% with Grade A"

def test_F():
    assert functions.grades("Frank", 1, 4, 71) == "Frank scored 43% with Grade E"

