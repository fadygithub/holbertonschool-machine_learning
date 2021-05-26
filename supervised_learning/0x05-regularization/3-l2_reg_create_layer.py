#!/usr/bin/env python3
"""Tensorflow layer Module"""

import tensorflow as tf


# prev is a tensor containing the output of the previous layer
# n is the number of nodes the new layer should contain
# activation is the activation function that should be used on the layer
# lambtha is the L2 regularization parameter


def l2_reg_create_layer(prev, n, activation, lambtha):
    """Returns the output of the new layer"""
    w = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    l2_regu = tf.contrib.layers.l2_regularizer(lambtha)
    layer = tf.layers.Dense(units=n, activation=activation,
                            kernel_initializer=w, name="layer",
                            kernel_regularizer=l2_regu)
    y = layer(prev)
    return (y)
