#!/usr/bin/env python3
"""A module that defines a neuron"""
import numpy as np


class Neuron:
    """Class Neuron"""
    def __init__(self, nx):
        """Class Initialization"""
        if type(nx) != int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Getter function for weights"""
        return self.__W

    @property
    def b(self):
        """Getter function for biases"""
        return self.__b

    @property
    def A(self):
        """Getter function for A"""
        return self.__A

    def forward_prop(self, X):
        """This will calculate the neuron's forward propagation"""
        Z = np.matmul(self.__W, X) + self.__b
        # Sigmoid activation function
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A

    def cost(self, Y, A):
        """This will calculate the model's cost function"""
        cost_array = np.multiply(np.log(A), Y) + np.multiply((
            1 - Y), np.log(1.0000001 - A))
        cost = -np.sum(cost_array) / len(A[0])
        return cost

    def evaluate(self, X, Y):
        """This will evaluate the predictions of the neurons"""
        self.forward_prop(X)
        cost = self.cost(Y, self.__A)
        return (np.where(self.__A > 0.5, 1, 0), cost)

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """This will calculate one pass of gradient descent"""
        cost = self.cost(Y, A)
        dz = A - Y
        dw = (1 / len(Y[0])) * np.matmul(dz, X.T)
        db = (1 / len(Y[0])) * np.sum(dz)
        self.__W = self.__W - alpha * dw
        self.__b = self.__b - alpha * db
