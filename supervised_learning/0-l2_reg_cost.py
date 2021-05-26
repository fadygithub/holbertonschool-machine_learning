#!/usr/bin/env python3
"""L2 regularization Module"""

import numpy as np

# cost is the cost of the network without L2 regularization
# lambtha is the regularization parameter
# weights is a dictionary of the weights and biases
# L is the number of layers in the neural network
# m is the number of data points used

def l2_reg_cost(cost, lambtha, weights, L, m):
    """Function L2 Regularization"""
    l2 = 0
    for i in range(1, L+1):
        w = "W" + str(i)
        l2 += 1/m * lambtha/2 * np.linalg.norm(weights[w])
    return cost + l2
