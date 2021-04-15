#!/usr/bin/env python3
"""Function for mat_mul"""


def mat_mul(mat1, mat2):
    """Multiplying two arrays"""
    if len(mat1[0]) != len(mat2):
        return None
    new_matrix = [[sum(a * b for a, b in zip(mat1_rows, mat2_column))
                for mat2_column in zip(*mat2)]
               for mat1_rows in mat1]
    return new_matrix
