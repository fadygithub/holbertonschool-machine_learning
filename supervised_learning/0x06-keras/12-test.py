#!/usr/bin/env python3
"""Neural network testing Module"""
import tensorflow.keras as K


def test_model(network, data, labels, verbose=True):
    """Function that returns loss & accuracy of our model"""
    return network.evaluate(data, labels, verbose=verbose)
