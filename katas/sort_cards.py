"""Implement module that will sort a deck of cards."""


def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank.

    sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
    ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    """
    deck = []
    alphas = []
    for card in cards:
        if card.isalpha():
            alphas.append(card)
        else:
            deck.append(card)
    deck = sorted(deck)
    for _ in range(alphas.count('A')):
        deck.insert(0, 'A')
    for _ in range(alphas.count('T')):
        deck.append('T')
    for _ in range(alphas.count('J')):
        deck.append('J')
    for _ in range(alphas.count('Q')):
        deck.append('Q')
    for _ in range(alphas.count('K')):
        deck.append('K')
    return deck
