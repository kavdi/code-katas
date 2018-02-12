"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice."""


def twoSum(nums, target):
    """take the two numbers out of the nums list that sum to the target num and return in a list."""
    answer = []
    x = len(nums) - 1
    for i in range(x):
        if nums[i] + nums[i + 1] == target:
            answer.append(nums[i])
            answer.append(nums[i + 1])
            return answer
        else:
            continue

"""Does not solve problem. Need to iterate through all numbers in the list if the first does not sum to the number."""