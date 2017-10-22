"""This is a file that tests the two_to_one function."""

import pytest

TWO_PARAMS = [("aretheyhere", "yestheyarehere", "aehrsty"), ("loopingisfunbutdangerous", "lessdangerousthancoding", "abcdefghilnoprstu"), ("inmanylanguages", "theresapairoffunctions", "acefghilmnoprstuy"), ("lordsofthefallen", "gamekult", "adefghklmnorstu"), ("codewars", "codewars", "acdeorsw"), ("agenerationmustconfrontthelooming", "codewarrs", "acdefghilmnorstuw")]

@pytest.mark.parametrize('n, x ,result', TWO_PARAMS)
def test_longest(n, x, result):
    """This function tests the longest function."""
    from two_to_one import longest
    assert longest(n, x) == result