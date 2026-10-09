#!/usr/bin/python3
"""Module that calculates the minimum operations to reach n characters."""


def minOperations(n):
    """Return the fewest operations needed to get exactly n H characters."""
    if not isinstance(n, int) or n < 2:
        return 0
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
