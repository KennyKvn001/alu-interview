#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    Calculate the minimum number of operations required to obtain
    a target integer from the input integer n.
    """
    if type(n) != int:
        return 0

    if n <= 1:
        return 0

    result = 0
    for i in range(2, int(n + 1)):
        while n % i == 0:
            result += i
            n //= i

    if n > 1:
        result += n

    return result
