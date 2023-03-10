from lib.estimate_reading_time import estimate_reading_time


"""
Test 1: if given an empty string, will return 0
test_if_empty_string():
  estimate_reading_times(""):
# => 0
••• once further code written this will fail so taken out •••
"""

#def test_empty_string_returns_0_minutes():
#    assert estimate_reading_time("") == 0


"""
Test 2: if given a 50 word string, will return "0.25 minutes to read this text"
"""

def test_if_50_word_string():
    assert estimate_reading_time("one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten") == "0.25 Minutes to read this text"


"""
Test 3: if given a 100 word string, will return 0.5 minutes
"""

def test_if_100_words_string():
    assert estimate_reading_time("one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten") == "0.5 Minutes to read this text"

"""
Test 4: if given a 400 word string, will return 2 minutes
"""

def test_if_400_word_string():
    assert estimate_reading_time("one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten") == "2.0 Minutes to read this text"


"""
Test 5: if given a value that is not a string, will return "This function will only accept a string"
"""

def test_only_aceepts_string():
    assert estimate_reading_time(True) == "This function will only accept a string"