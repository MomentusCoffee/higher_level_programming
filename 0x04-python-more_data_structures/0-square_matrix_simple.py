#!/usr/bin/python3
"""A function that computes the square value of all integers of a matrix from 0-main.py
"""
def square_matrix_simple(matrix=[]):
    if matrix:
        return [[y * y for y in x] for x in matrix]
