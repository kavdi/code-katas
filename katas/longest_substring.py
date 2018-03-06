"""Given a string, find the length of the longest substring without repeating characters."""


def lengthOfLongestSubstring(string):
    """Give back length of longest substring."""
    used = {}
    longest = start = 0
    for i, c in enumerate(string):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            longest = max(longest, i - start + 1)

        used[c] = i
    return longest
