"""This function takes two strings and gives you a string of the unique letters from each string, the best practice answer was: def longest(a1, a2):
    return "".join(sorted(set(a1 + a2))) """

def longest(s1, s2):
    """This function takes two strings and gives you a string of the unique letters from each string."""
    x = s1 + s2
    y = (''.join(set(x)))
    z = sorted(y)
    return ''.join(z)