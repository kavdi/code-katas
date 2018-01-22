""" Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as * """


def tower_builder(n_floors):
    """Build tower with * as floor."""
    b = '*'
    x = n_floors * 2 - 1
    l = []
    s = 1
    for i in range(n_floors):
        if x < n_floors * 2 - 1:
            l.append(' ' * s + b * x + ' ' * s)
            s += 1
        else:
            l.append(b * x)
        x -= 2
    l.reverse()
    return(l)
