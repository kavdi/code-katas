"""
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
"""


def persistence(n):
    """Get how many times you must multiply the digits within a number to get to a single digit."""
    num = n
    x = None
    answer = 0
    while len(str(num)) > 1:
        for i in str(num):
            if x is None:
                x = int(i)
            else:
                x = int(i) * x
        answer += 1
        num = x
        x = None
    return answer
