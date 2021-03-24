#!/usr/bin/python3
"""A function that prints a matrix of integers from 6-main.py
"""
def print_matrix_integer(matrix=[[]]):
        for row in matrix:
                print(' '.join(["{:d}".format(elem) for elem in row]))
