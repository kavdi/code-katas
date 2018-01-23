"""Create a function to remove all consecutive duplicate letters from each string."""


def dup(arry):
    """Remove all consecutive duplicate letters from each string."""
    answer = []
    for i in arry:
        x = list(i)
        cur = []
        for i in range(len(x) - 1):
            if x[i] != x[i + 1]:
                cur.append(x[i])
        cur.append(x[len(x) - 1])
        word = ''.join(cur)
        answer.append(word)
    return answer
