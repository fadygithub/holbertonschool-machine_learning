#!/usr/bin/env python3
"""Label vector to a one hot matrix Module"""

import tensorflow.keras as K


def one_hot(labels, classes=None):
    """Function that returns one hot matrix"""
    return K.utils.to_categorical(labels, num_classes=classes)
