import pytest
from problem_patterns.frequency_counter import valid_anagram

def test_valid_anagram():
    assert valid_anagram('anagram', 'nagaram') is True
    assert valid_anagram('rat', 'car') is False
    assert valid_anagram('a', 'ab') is False
    assert valid_anagram('aacc', 'cccx') is False
    assert valid_anagram('listen', 'silent') is True
    assert valid_anagram('hello', 'billion') is False
    assert valid_anagram('evil', 'vile') is True
    assert valid_anagram('fluster', 'restfulx') is False
    assert valid_anagram('dusty', 'study') is True
    assert valid_anagram('night', 'thingy') is False
