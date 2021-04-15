#!/usr/bin/env python3
"""Function for np_cat"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenate two Numpy arrays"""
    return(np.concatenate((mat1, mat2), axis=axis))
