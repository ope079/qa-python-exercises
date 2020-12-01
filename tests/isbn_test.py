import pytest
from exercises import isbn

def test_isbn():
    num_list =  [9,7,8,0,3,0,6,4,0,6,1,5]
    assert isbn.isbn(num_list) == 7