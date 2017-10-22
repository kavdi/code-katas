"""This file contains a function that gives you all multiples of 3 and 5 before the input number, the best practice solution was:
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)"""


def solution(number):
    """This function returns all multiples of 3 and 5 below the input number"""
    answer = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            answer += i
    return answer 