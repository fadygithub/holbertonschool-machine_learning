#!/usr/bin/env python3
"""Neural network with the Keras Module"""

import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """Function that returns a keras model"""
    inputs = K.Input(shape=(nx,))
    regularization = K.regularizers.l2(lambtha)
    x = K.layers.Dense(layers[0], activation=activations[0],
                       kernel_regularizer=regularization)(inputs)
    for i in range(1, len(layers)):
        x = K.layers.Dropout(1 - keep_prob)(x)
        x = K.layers.Dense(layers[i], activation=activations[i],
                           kernel_regularizer=regularization)(x)
    return K.Model(inputs=inputs, outputs=x)
