#!/usr/bin/python3
"""
Calculate the minimum number of operations needed to obtain exactly
n 'H' characters in a text file using only 'Copy All' and 'Paste'
operations.
"""


def minOperations(n):
    """Minimum operation

    Args:
        n (int): number

    Returns:
        int: number of operation
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
