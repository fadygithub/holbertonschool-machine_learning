#!/usr/bin/env python3
"""Function for np_slice"""


def np_slice(matrix, axes={}):
    """Slicing a matrix along an axes"""
    args = []
    list_axes = []
    max_value = max(axes.keys())
    for x in range(max_value + 1):
        list_axes.append(x)
    for y in list_axes:
        if y in axes.keys():
            sliced = slice(*axes[y])
        else:
            sliced = slice(None)
        args.append(sliced)
    return matrix[tuple(args)]
