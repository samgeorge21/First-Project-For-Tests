"""from lib.make_snippet import *

"""
Test 1: given a string of 5 words or less, returns the string.
"""

def test_make_snippet():
    result = make_snippet("One two three four five six seven")
    assert result == "One two three four five..."

"""
Test 2: given a string of more than 5 words, returns the first 5 words and '...' for the rest.
"""

def test_no_snippet_needed():
    result = make_snippet("One two three four five")
    assert result == "One two three four five"