import pytest
from applications import factorial

def test_factorial_one():
    assert factorial.fact(1) == 1

def test_factorial_0():
    assert factorial.fact(0) == 1

def test_factorial_five():
    assert factorial.fact(5) == 120