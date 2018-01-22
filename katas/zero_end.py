"""Write an algorithm that takes an list and moves all of the zeros to the end, preserving the order of the other elements."""


def move_zeros(array):
    """Take all zeros and put them at the end of the list."""
    x = []
    y = []
    for i in array:
        if i != 0 or i is False:
            x.append(i)
        else:
            y.append(int(i))
    return(x + y)
