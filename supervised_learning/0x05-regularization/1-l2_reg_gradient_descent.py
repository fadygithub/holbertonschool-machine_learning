#!/usr/bin/env python3

"""Weights and biases Update Module"""

import numpy as np


# Y is a one-hot numpy.ndarray of shape (classes, m) that contains the correct labels for the data
# classes is the number of classes
# m is the number of data points
# weights is a dictionary of the weights and biases of the neural network
# cache is a dictionary of the outputs of each layer of the neural network
# alpha is the learning rate
# lambtha is the L2 regularization parameter
# L is the number of layers of the network


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """Function for gradient descent with L2 regularization technique"""
    weights_copy = weights.copy()
    dz = cache["A" + str(L)] - Y
    for i in range(L, 0, -1):
        A = cache["A" + str(i - 1)]
        w = "W" + str(i)
        b = "b" + str(i)
        dw = (1 / len(Y[0])) * np.matmul(dz, A.T) + 1/len(
            Y[0]) * lambtha * weights[w]
        db = (1 / len(Y[0])) * np.sum(dz, axis=1, keepdims=True)
        weights[w] = weights[w] - alpha * dw
        weights[b] = weights[b] - alpha * db
        dz = np.matmul(weights_copy["W" + str(i)].T, dz) * (1 - A * A)
