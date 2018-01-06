"""Test sort cards module."""
import pytest


D_PARAMS = [(list('39A5T824Q7J6K'), list('A23456789TJQK')), (list('Q286JK395A47T'), list('A23456789TJQK')), (list('54TQKJ69327A8'), list('A23456789TJQK'))]


@pytest.mark.parametrize('cards, deck', D_PARAMS)
def test_sort_cards(cards, deck):
    """Test card sorting function."""
    from sort_cards import sort_cards
    assert sort_cards(cards) == deck
