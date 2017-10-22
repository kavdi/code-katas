"""This is a file that tests the sum_of_lowest_int function."""

import pytest

S_PARAMS = [([5, 8, 12, 18, 22], 13), ([7, 15, 12, 18, 22], 19), ([25, 42, 12, 18, 22], 30), ([1, 8, 12, 18, 5], 6), ([13, 12, 5, 61, 22], 17)]


@pytest.mark.parametrize('n, result', S_PARAMS)
def test_sum_two_smallest_numbers(n, result):
    """This function tests the sum_of_smallest_numbers function."""
    from sum_of_lowest_int import sum_two_smallest_numbers
    assert sum_two_smallest_numbers(n) == result