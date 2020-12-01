import pytest
from exercises import near

def near_test():
    assert near.near("reset", "rest") == "True"

def near_test_false():
    assert near.near("resett", "rest") == "False"
