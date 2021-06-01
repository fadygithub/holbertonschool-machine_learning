#!/usr/bin/env python3
"""Weights loading and saving Module"""
import tensorflow.keras as K


def save_weights(network, filename, save_format='h5'):
    """Function that save sour weights"""
    network.save_weights(filename, save_format=save_format)
    return None


def load_weights(network, filename):
    """Function that loads our weights"""
    network.load_weights(filename)
    return None
