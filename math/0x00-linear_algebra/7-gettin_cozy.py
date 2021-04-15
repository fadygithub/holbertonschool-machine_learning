#!/usr/bin/env python3
"""Function for cat_matrices2D"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenation of two matrix"""
    new_matrix = []
    if axis == 0 and len(mat1[0]) == len(mat2[0]):
        for x in mat1:
            new_matrix.append(x[:])
        for rows in mat2:
            new_matrix.append(rows[:])
        return new_matrix
    if axis == 1 and len(mat1) == len(mat2):
        for rows in range(len(mat1)):
            new_matrix.append(mat1[rows] + mat2[rows])
        return new_matrix
    return None
