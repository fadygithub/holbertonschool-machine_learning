#!/usr/bin/env python3
"""Keras loading an dsaving Module"""
import tensorflow.keras as K


def save_model(network, filename):
    """Function that saves our model"""
    network.save(filename)
    return None


def load_model(filename):
    """Function that loads our model"""
    return K.models.load_model(filename)
