"""
take a given string and reverse the order of the words.
You may assume that the string is a sentence that contains only letters and spaces,
with all words separated by one space.
"""
def word_reverser(phrase):
  return " ".join(phrase.split()[::-1])