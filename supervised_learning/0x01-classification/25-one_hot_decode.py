#!/usr/bin/env python3

"""One hot matrix to vector of labels conversion"""

import numpy as np


def one_hot_decode(one_hot):
    """Vector conversion"""
    if type(one_hot) is not np.ndarray or len(one_hot) == 0:
        return None
    if len(one_hot.shape) != 2:
        return None
    return np.argmax(one_hot, axis=0)
