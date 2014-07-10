#!/usr/bin/env python2
from time import time
from math import factorial

def comb(n, r):
    return factorial(n) / (factorial(r)) / factorial(n - r)

t0 = time()
total = 0

for n in range(101):
    for r in range(n + 1):
        c = comb(n, r)
        if c > 1000000:
            total +=1
t1 = time()
print total
print '**time**:', t1 - t0

