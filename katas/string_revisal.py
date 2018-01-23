"""Create a function to remove all consecutive duplicate letters from each string."""


def dup(arry):
    """Remove all consecutive duplicate letters from each string."""
    answer = []
    for i in arry:
        x = list(i)
        z = 0
        import pdb; pdb.set_trace()
        while z < len(x) - 1:
            if x[z] == x[z + 1]:
                x.remove(x[z + 1])
            else:
                print(len(x))
                print(x)
                z += 1
        x = ''.join(x)
        answer.append(x)
    return answer


def dup2(arry):
    answer = []
    cur = []
    for i in arry:
        x = list(i)
        z = 0
        import pdb; pdb.set_trace()
        while z < len(x) - 1:
            if x[z] != x[z + 1]:
                cur.append(x[z])
            elif x[z] == x[z + 1]:
                z += 1
        word = ''.join(cur)
        answer.append(word)
        cur = []
    return answer
