#!/usr/bin/env python3
"""Function for matrix_transpose"""


def matrix_transpose(matrix):
    """Transposing a matrix"""
    new_matrix = []
    for columns in range(len(matrix[0])):
        transpose = []
        for rows in range(len(matrix)):
            transpose.append(matrix[rows][columns])
        new_matrix.append(transpose)
    return new_matrix
