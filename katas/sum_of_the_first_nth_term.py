"""This module contains a function that returns the nth sum, the best practice solution was: def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))."""

def series_sum(n):
    """This function returns the nth sum to the 2nd decimal place."""
    x = 4
    y = 1
    if n == 0:
        return str("%.2f" % 0)
    if n == 1:
        return str("%.2f" % 1)
    else:
        for i in range(n - 1):
            y += (1 / x)
            x += 3
    return str("%.2f" % y)
