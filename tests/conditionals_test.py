import pytest
from exercises import conditionals

def test_conditional_Fail():
    assert conditionals.grades(64) == 'Fail'

def test_conditional_pass():
    assert conditionals.grades(67) == 'Pass'

def test_conditional_distinction():
    assert conditionals.grades(89) == 'Distinction'