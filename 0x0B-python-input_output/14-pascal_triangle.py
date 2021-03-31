#!/usr/bin/python3
"""
Creates pascal's triangle


"""


def pascal_triangle(n):
    """
    Creates pascal's triangle

    Args:
        n: number of rows to create

    Returns:
        pascal's triangle
    """
    if n <= 0:
        return []
    tri = [[1]] # first row is always 1
    for row in range(1, n): # for every other row
        i = [1] # starts each new row with 1
        for col in range(1, row): # for all the others:
            i.append(tri[row - 1][col - 1] + tri[row - 1][col]) # work out what the number is
        i.append(1) # row always ends in 1
        tri.append(i) # add the row in matrix
    return tri
