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

    def prime_factors(num):
        result = []
        for i in range(2, int(num**0.5) + 1):
            while num % i == 0:
                result.append(i)
                num //= i

        if num > 1:
            result.append(num)

        return result

    result = prime_factors(n)
    return sum(result)
