"""Given two list of strings, return the number of times each string of the second array appears in the first array."""


def solve(a, b):
    """Check lists for matching strings."""
    answer = []
    x = 0
    for i in b:
        for y in a:
            if i == y:
                x += 1
        answer.append(x)
        x = 0
    return answer
