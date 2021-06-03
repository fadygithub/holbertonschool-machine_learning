#!/usr/bin/env python3
"""Convolution on grayscale images Module"""

import numpy as np


def convolve_grayscale_valid(images, kernel):
    """Function that returns a numpy array with the convolved images"""
    w, h, m = images.shape[2], images.shape[1], images.shape[0]
    kw, kh = kernel.shape[1], kernel.shape[0]
    new_h = int(h - kh + 1)
    new_w = int(w - kw + 1)
    output = np.zeros((m, new_h, new_w))
    for x in range(new_w):
        for y in range(new_h):
            output[:, y, x] = (kernel * images[:,
                                               y: y + kh,
                                               x: x + kw]).sum(axis=(1, 2))
    return output
