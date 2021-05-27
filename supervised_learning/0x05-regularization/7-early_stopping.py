#!/usr/bin/env python3
"""Gradient Descent stop Module"""
# cost is the current validation cost of the neural network
# opt_cost is the lowest recorded validation cost of the neural network
# threshold is the threshold used for early stopping
# patience is the patience count used for early stopping
# count is the count of how long the threshold has not been met


def early_stopping(cost, opt_cost, threshold, patience, count):
    """Function that returns a boolean to stop the training"""
    if (opt_cost - cost) <= threshold:
        if count + 1 >= patience:
            return True, count + 1
        else:
            return False, count + 1
    else:
        return False, 0
