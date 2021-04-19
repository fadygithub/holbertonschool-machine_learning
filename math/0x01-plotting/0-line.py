#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y_axis = np.arange(0, 11) ** 3

plt.plot(y_axis, 'r-')
plt.xlim(0, 10)
plt.show()
