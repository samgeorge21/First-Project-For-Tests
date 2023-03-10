import pytest 
from lib.count_words import *

"""
Test 1: test function returns a string
"""

#def test_function_returns_string():
#    result = count_word("test")
#    assert result == "test"

"""
Test 2: function counts words in a string
"""

def test_function_counts_string_words():
    assert count_words("one") == 1

"""
Test 3: function counts multiple words in a string
"""

def test_counts_multi_words():
    assert count_words("one two") == 2

"""
Test 4: empty string returns zero
"""

def test_empty_returns_nil():
    assert count_words("") == 0

"""
Test 5: function returns error if non-string entered
"""

#def test_not_string_error():
#    assert count_words(77) == "This function is not a string"