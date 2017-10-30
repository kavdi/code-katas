"""Check for parentheses."""


def parenthese_pairs(sentense):
    """Check to see if all openned parentheses are closed."""
    openned = 0
    closed = 0
    for i in sentense:
        if i == '(':
            openned += 1
        elif i == ')':
            closed += 1
    if openned == closed:
        return 0
    if openned > closed:
        return 1
    if openned < closed:
        return -1
