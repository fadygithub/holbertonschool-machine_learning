#!/usr/bin/env python3
"""Function add_matrices2D"""


def add_matrices2D(mat1, mat2):
    """Addition of two arrays"""
    if len(mat1[0]) != len(mat2[0]):
        return None
    new_matrix = []
    for rows in range(len(mat1)):
        arr = []
        for columns in range(len(mat1[0])):
            arr.append(mat1[rows][columns] + mat2[rows][columns])
        new_matrix.append(arr)
    return new_matrix
