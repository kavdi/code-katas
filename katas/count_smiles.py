"""Function that finds how many smiley faces are in a given list."""


def count_smileys(arr):
    """Find how many smiley faces are in the given list."""
    a = set([':)', ':~)', ':-)', ';)', ';~)', ';-)', ':D', ':-D', ':~D', ';D', ';-D', ';~D'])
    answer = 0
    for i in arr:
        if i in a:
            answer += 1
    return answer
