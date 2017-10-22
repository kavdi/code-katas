"""This is a file that tests the love_vs_friendship function."""

import pytest

LF_PARAMS = [('knowledge', 96), ('selfness', 99), ('family', 66), ('friends', 75), ('attitude', 100), ('khilqdklfsj', 119), ('hihesvroplmxkvc', 205), ('foghmlvycccpbjnmvq', 211), ('agpxw', 71), ('dsnrxf', 85)]


@pytest.mark.parametrize('n, result', LF_PARAMS)
def test_words_to_marks(n, result):
    """This function tests the words_to_marks function."""
    from love_vs_friendship import words_to_marks
    assert words_to_marks(n) == result