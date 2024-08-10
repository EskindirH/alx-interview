#!/usr/bin/python3
"""

This module calculates Pascal's triangle.

"""

def pascal_triangle(n):
    """Pascal triangle function.

    Args:
        n (int): Number of rows.

    Returns:
        List: list of lists of integer
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
