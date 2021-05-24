#!/usr/bin/env python3
"""Sensitivity Module"""

import numpy as np


def sensitivity(confusion):
    """FUnction that will return the sensitivity"""
    return np.sum((confusion * np.identity(
        confusion.shape[0])) / np.sum(confusion, axis=1), axis=1)
