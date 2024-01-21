#!/usr/bin/python3
""" Minimumu operation"""
import math


def minOperations(n):
    """Calculations"""
    if type(n) != int:
        return 0

    if n <= 1:
        return 0

    result = 0
    for i in range(2, int(math.sqrt(abs(n + 1))):
        while n % i == 0:
            result += i
            n //= i

    if n > 1:
        result += n

    return result
