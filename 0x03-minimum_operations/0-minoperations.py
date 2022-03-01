#!/usr/bin/python3
"""Minimum operations module"""


def minOperations(n):
    """Returns the minimum number of operations to copy/paste
    a single letter to n letters
    Args:
        n (int): The number of operations
    Returns:
        int: an integer
    """
    if type(n) is not int or n < 2:
        return 0
    result = 0
    iteration = 2
    while n > 1:
        if n % iteration == 0:
            result += iteration
            n /= iteration
        else:
            iteration += 1
    return result
