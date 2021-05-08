#!/usr/bin/env python3
"""A module that define a neuron"""
import numpy as np


class Neuron:
    """Class Neuron"""
    def __init__(self, nx):
        """Data initialization"""
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
