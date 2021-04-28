#!/usr/bin/env python3
"""Module for normal distribution"""


class Normal:
    """ Class normal"""
    def __init__(self, data=None, mean=0., stddev=1.):
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            else:
                self.mean = float(mean)
                self.stddev = float(stddev)
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self.mean = (sum(data) / len(data))
                s = 0
                for x in range(0, len(data)):
                    s = s + ((data[x] - self.mean))**2
                self.stddev = (s/len(data))**(1/2)

    def z_score(self, x):
        """Z-score calculation"""
        return ((x - self.mean) / self.stddev)

    def x_value(self, z):
        """x-score calculation"""
        return self.stddev * z + self.mean

    def pdf(self, x):
        """PDF calculation"""
        return (2.7182818285**((-1/2) * (((
            x - self.mean) / self.stddev)**2))) * (
            1 / (self.stddev * (2 * 3.1415926536) ** (1/2)))

    def cdf(self, x):
        """CDF calculation"""
        num = (x - self.mean) / (self.stddev * (2**(1/2)))
        erf = (2 / (3.1415926536**(1/2))) * (num - (num**3)/3 + (
            num**5)/10 - (num**7)/42 + (num**9)/216)
        return (1 / 2) * (1 + erf)
