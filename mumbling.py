"""This is a code wars kata that takes a string and returns a longer string with the letters multiplied by the position they hold in the string. The best practice solution was : def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))"""

def accum(s):
    """This function takes in a string and returns a longer string with each letter multiplied by the position it holds."""
    first = []
    other = []
    second = []
    third = []
    answer = []
    answer2 = ''
    number = 0
    for i in s:
        first.append(i.lower())
    for h in first:
      number += 1
      other.append(number)
    for i in other:
      second.append(first[i-1] * i)
    for i in second:
      third.append(i.capitalize())
    answer.append("-".join(third))
    return (answer2.join(answer))



#7kyu