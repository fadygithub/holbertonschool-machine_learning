#!/usr/bin/env python3
"""Mini batch gradient descent Module"""
import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                verbose=True, shuffle=False):
    """Function that returns history object"""
    History = network.fit(
                        x=data,
                        y=labels,
                        batch_size=batch_size,
                        epochs=epochs,
                        verbose=verbose,
                        shuffle=shuffle)
    return History
