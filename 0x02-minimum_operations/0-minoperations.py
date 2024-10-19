#!/usr/bin/python3
"""
Defines the minOperations function that calculates the fewest number of
operations to achieve n H characters using only Copy All and Paste operations.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to result in
    exactly n H characters.
    If n is impossible to achieve, return 0.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The fewest number of operations required.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        # While n is divisible by the factor, divide and add operations
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
