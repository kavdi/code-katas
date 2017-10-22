"""This file has a function that sums a list but ignores the duplicates, the best practice solution was: 
from collections import Counter
def sum_no_duplicates(nums):
    return sum(k for k, v in Counter(nums).items() if v == 1)"""

def sum_no_duplicates(l):
    """This function returns the sum of a list but ignores all duplicates."""
    y = [x for x in l if l.count(x) < 2]
    return sum(y)