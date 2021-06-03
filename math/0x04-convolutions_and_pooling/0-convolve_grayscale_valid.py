#!/usr/bin/env python3
"""Convolution on grayscale images Module"""

import numpy as np


def convolve_grayscale_valid(images, kernel):
     """Function that returns a numpy array with the convolved images"""
    m, h, w = images.shape
    kh, kw = kernel.shape
    conv = np.zeros((m, h - kh + 1, w - kw + 1))
    for row in range(conv.shape[1]):
        for column in range(conv.shape[2]):
            sub_matrix = images[:, row: row + kh, column: column + kw]
            conv[:, row, column] = (sub_matrix * kernel).sum(axis=(1, 2))
    return conv
