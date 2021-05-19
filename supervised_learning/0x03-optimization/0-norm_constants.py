#!/usr/bin/env python3
"""norm_constants Module"""

import numpy as np


def normalization_constants(X):
    """Function that will return the mean and standard deviation of the inputs"""
    mean = np.mean(X, axis=0)
    stdev = np.std(X, axis=0)
    return mean, stdev

