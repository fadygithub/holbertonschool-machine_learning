#!/usr/bin/env python3
"""F1 Score Calculation Module"""


import numpy as np
sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """Function that returns the F1 score"""
    return 2 * (sensitivity(confusion) * precision(confusion)) / (
        sensitivity(confusion) + precision(confusion))
