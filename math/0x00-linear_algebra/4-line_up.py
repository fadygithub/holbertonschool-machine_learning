#!/usr/bin/env python3
"""Function add_arrays"""


def add_arrays(arr1, arr2):
    """Addition of two arrays"""
    if len(arr1) != len(arr2):
        return None
    arr_addition = []
    for x in range(len(arr1)):
        arr_addition.append(arr1[x] + arr2[x])
    return arr_addition
