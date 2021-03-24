#!/usr/bin/python3
"""A function that divides all elements of a matrix from 2-main.py
Usage: ./main-py
Edge Case: python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
"""


def matrix_divided(matrix, div):
    """
    Defines how division is performed in matrix

    Args:
        matrix: 2d array
        div: int used for division of matrix

    Return:
        new matrix
    """
    if not isinstance(matrix, (list, (int, float))) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(x) == len(next(iter(matrix))) for x in iter(matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(y / div) for y in x] for x in matrix]
