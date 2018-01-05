"""Test proper_parenthetics module."""

import pytest
from proper_parenthetics import parenthese_pairs

P_PARAMAS = [
    ('abc(dsdf)dfsdf(sdfsdfs)sdfsdf(sdfs)', 0),
    ('(()(()(', 1),
    ('()()))())' -1),
    (')))(((', -1),
    ('()((())', 1),
    ('()((())))()' -1),
    ('()()(())(' -1)
]


@pytest.mark.parametrize('str, output', P_PARAMAS)
def test_parnthese_pairs_returns_correct_output(str, output):
    """Test that given a string with parentheses you will get correct output."""
    assert parenthese_pairs(str) == output
