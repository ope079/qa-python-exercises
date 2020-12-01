import pytest
from exercises import best_conjugation

def test_fitting():
    assert best_conjugation.conjugation("fitting") == 13

def test_sat():
    assert best_conjugation.conjugation("sat") == 6