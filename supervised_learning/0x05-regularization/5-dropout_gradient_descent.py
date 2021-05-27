#!/usr/bin/env python3
"""Dropout regularization using gradient descent Module"""
import numpy as np


# Y is a one-hot numpy.ndarray of shape (classes, m) that contains the correct labels for the data
# classes is the number of classes
# m is the number of data points
# weights is a dictionary of the weights and biases of the neural network
# cache is a dictionary of the outputs and dropout masks of each layer of the neural network
# alpha is the learning rate
# keep_prob is the probability that a node will be kept
# L is the number of layers of the network


def dropout_gradient_descent(Y, weights, cache, alpha, keep_prob, L):
    """weights of the network should be
       updated in place"""
    dz = cache["A" + str(L)] - Y
    for i in range(L, 0, -1):
        A = cache["A" + str(i - 1)]
        dw = (1 / len(Y[0])) * np.matmul(dz, A.T)
        db = (1 / len(Y[0])) * np.sum(dz, axis=1, keepdims=True)
        w = "W" + str(i)
        b = "b" + str(i)
        if i != 1:
            d = "D" + str(i - 1)
            da = np.matmul(weights[w].T, dz)
            dz = da * (1 - (A**2)) * (cache[d] / keep_prob)
        weights[w] = weights[w] - alpha * dw
        weights[b] = weights[b] - alpha * db
