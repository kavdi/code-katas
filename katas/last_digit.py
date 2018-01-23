"""Module for function that takes in two numbers a and b and returns the last decimal digit of a^b."""


def last_digit(n1, n2):
    """Return last digit of n1^n2."""
    x = n1 ** n2
    answer = int(repr(x)[-1])
    return answer
 

 """This is not working for large numbers. Need to refactor code to work properly."""