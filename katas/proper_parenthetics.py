"""Check for parentheses."""


def parenthese_pairs(sentnese):
    """Check to see if all openned parentheses are closed."""
    o = '('
    c = ')'
    s = list(sentnese)
    balance = 0
    if s[0] == c:
        balance = -1
        return balance
    if s[len(s) - 1] == o:
        balance = 1
        return balance
    for i in s:
        if balance >= 0:
            if i == o:
                balance += 1
            elif i == c:
                balance -= 1
        elif balance < 0:
            balance = -1
            return balance
    return balance
