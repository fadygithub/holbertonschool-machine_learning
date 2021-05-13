#!/usr/bin/env python3
"""Create a Layer Modulemod"""

import tensorflow as tf


def create_layer(prev, n, activation):
    """Create Layer function"""
    weight = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    layer = tf.layers.Dense(units=n, activation=activation,
                            kernel_initializer=weight, name="layer")
    y = layer(prev)
    return (y)
