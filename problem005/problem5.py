#!/usr/bin/env python2
from math import sqrt
from operator import mul

def euclid(x, y):
    y, x = x, y % x
    while x > 0:
        y, x = x, y % x
    return y

def mcm(x, y):
    return y * x / euclid(x, y)


print reduce(mcm, xrange(2, 21))
