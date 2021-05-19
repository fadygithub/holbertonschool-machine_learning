#!/usr/bin/env python3
"""RMSProp Module"""
import numpy as np


def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):
    """Function that returns an updated variable & gradient"""
    Sdw = beta2 * s + (1 - beta2) * (grad**2)
    W = var - alpha * grad / (Sdw ** (1/2) + epsilon)
    return W, Sdw
