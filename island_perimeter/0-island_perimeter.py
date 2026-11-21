#!/usr/bin/python3
"""Module that computes the perimeter of an island described in a grid."""


def island_perimeter(grid):
    """Return the perimeter of the island described in grid.

    grid is a list of lists of integers:
        0 represents water
        1 represents land
    Each cell is a square with a side length of 1, and cells are connected
    horizontally or vertically only.
    """
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                perimeter += 4
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
