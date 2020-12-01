import pytest
from exercises import grade_calculator

def test_grade():
    assert grade_calculator.grade_calc(70,80,90) == "Your percentage score is 80%\nYou scored a grade of : A"