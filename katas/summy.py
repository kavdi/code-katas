"""This file contains a function that adds numbers that are in a string and gives the sum, the best practice solution was def summy(string_of_ints):
    return sum(map(int,string_of_ints.split()))"""


def summy(string_of_ints):
    """This function takes a string of numbers with spaces and returns the sum of the numbers."""
    numbers = string_of_ints.split()
    answer = 0
    for i in numbers:
      answer = answer + int(i)
    return answer
