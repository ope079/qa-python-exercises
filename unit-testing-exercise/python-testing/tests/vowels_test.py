import pytest
from applications import vowels

def vowels_one():
    assert vowels.vowels("one") == 2

def vowels_africa():
    assert vowels.vowels("africa") == 3

def vowels_none():
    assert vowels.vowels("rcdgnth") == 0

def vowels_all():
    assert vowels.vowels("aeiou") == 5