#!/usr/bin/env python3
"""normalization Module"""

import numpy as np


def normalize(X, m, s):
    """Function to normalize a matrix"""
    X = (X - m) / s
    return X
