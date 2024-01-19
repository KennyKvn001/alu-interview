#!/usr/bin/python3

""" Minimumu operation, a method that calculates
    the fewest number of operations needed to result
    in exactly n H characters in the file.
"""


def minOperations(n):
    """Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if n == 1:
        return 0

    result = 0
    for i in range(2, n + 1):
        while n % i == 0:
            result += i
            n //= i

    return result
