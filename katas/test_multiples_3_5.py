"""This is a file that tests the multiples_3_5 function."""

import pytest

M_PARAMS = [(10, 23), (20, 78), (0, 0), (1, 0), (200, 9168), ]


@pytest.mark.parametrize('n, result', M_PARAMS)
def test_solution(n, result):
    """This function tests the solution function."""
    from multiples_3_5 import solution
    assert solution(n) == result