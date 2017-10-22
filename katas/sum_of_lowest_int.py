"""This file contains a function that adds the two lowest intergers in a list of intergers,
the best solution was: def sum_two_smallest_numbers(numbers):return sum(sorted(numbers)[:2])"""

def sum_two_smallest_numbers(numbers):
    """This function takes a list of numbers and adds the two lowest intergers and returns the value"""
    b = []
    for x in range(2):
        d = min(int(s) for s in numbers) 
        b.append(d)
        numbers.remove(d)
    g = sum(b)
    return g


#7kyu