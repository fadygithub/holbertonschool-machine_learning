#!/usr/bin/env python3
"""norm_constants Module"""

import numpy as np


def normalization_constants(X):
    """Function that returns the mean &  standard deviation"""
    mean = np.mean(X, axis=0)
    stdev = np.std(X, axis=0)
    return mean, stdev
