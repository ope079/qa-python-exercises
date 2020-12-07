import pytest
from challenge_of_the_day import whitespace_sequence

def test_seperated():
    assert whitespace_sequence.seperated("hello world and practice makes perfect and hello world again") == "again and hello makes perfect practice world"

def test_seperated_2():
    assert whitespace_sequence.seperated("hello world a1nd practice makes perfect a2nd hello world again") == "a1nd a2nd again hello makes perfect practice world"