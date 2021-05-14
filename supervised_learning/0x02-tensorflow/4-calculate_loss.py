#!/usr/bin/env python3

"""Loss Calculation Module"""

import tensorflow as tf


def calculate_loss(y, y_pred):
    """Loss Calculation Function"""
    loss = tf.losses.softmax_cross_entropy(y, y_pred)
    return loss
