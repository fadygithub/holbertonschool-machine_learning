#!/usr/bin/env python3
"""Function for matrix_shape"""

def matrix_shape(matrix):
    """Checking the shape of the given matrix"""
    dimension = [len(matrix)]
    while type(matrix[0]) != int:
        dimension.append(len(matrix[0]))
        matrix = matrix[0]
    return dimension
