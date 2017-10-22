"""This is a file that tests the summy function."""

import pytest

Y_PARAMS = [("1 2 3", 6), ("1 2 3 4", 10), ("1 2 3 4 5", 15), ("10 10", 20), ("0 0", 0)]


@pytest.mark.parametrize('n, result', Y_PARAMS)
def test_summy(n, result):
    """This function tests the summy function."""
    from summy import summy
    assert summy(n) == result