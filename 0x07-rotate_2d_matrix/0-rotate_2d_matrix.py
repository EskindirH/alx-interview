#!/usr/bin/python3
"""
This module provides a function to rotate an n x n 2D matrix
90 degrees clockwise in place.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in place.

    The function modifies the matrix in place without using any additional
    space for another matrix.

    Args:
        matrix (list of list of int): 2D matrix to be rotated.

    Returns:
        None: The matrix is modified in place.
    """
    n = len(matrix)

    # Transpose the matrix: swap elements across the diagonal.
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the 90-degree clockwise rotation.
    for i in range(n):
        matrix[i].reverse()
