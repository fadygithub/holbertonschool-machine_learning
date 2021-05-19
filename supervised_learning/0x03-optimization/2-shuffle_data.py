#!/usr/bin/env python3
"""Data Shuffling Module"""

import numpy as np


def shuffle_data(X, Y):
    """Function that returns shuffled X & Y matrices"""
    perm = X.shape[0]
    shuff_op = np.random.permutation(perm)
    return X[shuff_op], Y[shuff_op]
