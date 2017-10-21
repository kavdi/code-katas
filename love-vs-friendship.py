"""This file contains a function that takes a word and gives you its value depending on how much the letter is wort a-z where a=1 b=2 c=3... the best practice was solution: def words_to_marks(s):return sum(ord(c)-96 for c in s)"""


import string
def words_to_marks(s):
    """This functio taks a string and gives you an int value for the string where a=1 b=2..."""
    number = 0
    values = dict()
    for index, letter in enumerate(string.ascii_lowercase):
       values[letter] = index + 1
    for i in s:
        number = number + values[i]
    return number