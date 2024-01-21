#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    Calculate and return the minimum number of operations
    needed to result in exactly n H characters in the file.
    """
    if type(n) != int:
        return 0

    if n <= 1:
        return 0

    def prime_factors(num):
        """
        Calculate and return the prime factors of the given number.

        :param num: int - the number for which to find prime factors
        :return: list - a list of the prime factors of the input number
        """
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
