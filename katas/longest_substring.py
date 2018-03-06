"""Given a string, find the length of the longest substring without repeating characters."""


def lengthOfLongestSubstring(string):
    """Give back length of longest substring."""
    used = {}
    max_length = start = 0
    for i, c in enumerate(string):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_length = max(max_length, i - start + 1)

        used[c] = i
    return max_length
