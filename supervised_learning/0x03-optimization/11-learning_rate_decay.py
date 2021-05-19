#!/usr/bin/env python3
"""Learning Rate Decay Module"""
import numpy as np


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """"Function that returns an updated value for the learning rate alpha"""
    return alpha / (1 + decay_rate * np.floor(global_step / decay_step))
