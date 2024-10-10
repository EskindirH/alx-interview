#!/usr/bin/python3
"""
Calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    The grid is a rectangular list of lists where:
    - 0 represents water.
    - 1 represents land.
    Each cell is square, with side length of 1.
    Cells are connected horizontally/vertically but not diagonally.

    Parameters:
    grid (list of list of int): The grid representing the island and water.

    Returns:
    int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Add 4 for a land cell
                perimeter += 4

                # Check if the cell above is also land, subtract 2 if true
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

                # Check if the cell to the left is also land, subtract 2 if true
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
