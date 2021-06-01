#!/usr/bin/env python3
"""Analyze data validation Module"""
import tensorflow.keras as K


def train_model(network, data, labels, batch_size,
                epochs, validation_data=None,
                verbose=True, shuffle=False):
    """Function that returns history"""
    History = network.fit(
                        x=data,
                        y=labels,
                        batch_size=batch_size,
                        epochs=epochs,
                        verbose=verbose,
                        shuffle=shuffle,
                        validation_data=validation_data)
    return History
