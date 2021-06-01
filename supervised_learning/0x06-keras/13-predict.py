#!/usr/bin/env python3
"""Prediction Module"""
import tensorflow.keras as K


def predict(network, data, verbose=False):
    """Function that returns our prediction"""
    return network.predict(data, verbose=verbose)
