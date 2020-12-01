import pytest
import count_example.count as count

def test_count_zeros():
    assert count.count([0, 0, 0], 0) == 3

def test_count_string():
    assert count.count(["a", "a", "a"], "a") == 3