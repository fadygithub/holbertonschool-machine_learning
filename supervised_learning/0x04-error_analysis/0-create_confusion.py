#!/usr/bin/env python3
"""Confusion Matrix Module"""

import numpy as np


def create_confusion_matrix(labels, logits):
    """FUnction to create a confusion matrix"""
    return np.matmul(labels.T, logits)
