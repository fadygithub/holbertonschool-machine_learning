#!/usr/bin/env python3

"""Training Operation Module"""

import tensorflow as tf


def create_train_op(loss, alpha):
    """Training Operation Function"""
    optimizer = tf.train.GradientDescentOptimizer(alpha)
    train = optimizer.minimize(loss)
    return train
