#!/usr/bin/python3
"""
function that computes the square value of all integers of a matrix.
"""


def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = []
        for row in matrix:
            new_matrix.append([item ** 2 for item in row])
        return new_matrix
    else:
        return matrix