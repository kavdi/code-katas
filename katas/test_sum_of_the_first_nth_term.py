"""This module tests the sum_of_the_nth_term module"""

import pytest


S_PARAMS = [(1, "1.00"), (2, "1.25"), (3, "1.39"), (4, "1.49"), (5, "1.57"), (6, "1.63"), (7, "1.68"), (8, "1.73"), (9, "1.77"), (15, "1.94"), (39, "2.26"), (0, "0.00"), (58, "2.40")]


@pytest.mark.parametrize('n, result', S_PARAMS)
def test_series_sum(n, result):
    """This function tests the series_sum function."""
    from sum_of_the_first_nth_term import series_sum
    assert series_sum(n) == result