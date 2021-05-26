#!/usr/bin/env python3
"""Cost Calculation Module"""

import tensorflow as tf


def l2_reg_cost(cost):
    """Function taht calculates the cost"""
    regularization_losses = tf.losses.get_regularization_losses()
    return cost + regularization_losses
