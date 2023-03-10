Example recipe:

1. Describe the problem

As a user, so that I can manage my time, I want to see an estimate of reading time for a text, assuming a reading speed of 200 words per minute, e.g. text of 100 words would take .05 minutes

2. Design the function signature

def estimate_reading_time(text):
  parameters:
    text: a string containing multiple words
  return value:
    the number of minutes taken to read a text as a float
  side effects:
    this function doesn't have any side effects

3. Example tests:

"""
Test 1: if given an empty string, will return 0 minutes
test_if_empty_string():
  estimate_reading_times(""):
# => "0 minutes"

Test 2: if given a 50 word string, will return 0.25 minutes
test_if_50_word_string():
  estimate_reading_times("one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten"):
# => "0.25 minutes"

Test 3: if given a 100 word string, will return 0.5 minutes
test_if_100_words_string():
  estimate_reading_times("one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten"):
# => "0.5 minutes"

Test 4: if given a 400 word string, will return 2 minutes
test_if_400_word_string():
  estimate_reading_times("one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten"):
# => "2 minutes"

Test 5: if given a value that is not a string, will return "This function will only accept a string"
estimate_reading_time(True):
# => "This function will only accept a string"
"""

4. Implement behaviour:
After each test you write, follow the test-driving process or red, green, refactor to implement the behaviour.