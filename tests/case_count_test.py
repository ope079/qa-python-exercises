import pytest
from challenge_of_the_day import case_count

def test_count():
    assert case_count.case_count("Hello world!") == "UPPER CASE 1 \nLOWER CASE 9"