import pytest
from dice import throw

def throw_test():
    assert throw.generate() > 0 and throw.generate() <= 6