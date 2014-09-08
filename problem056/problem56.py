#!/usr/bin/env python2
import itertools as  it
from time import time


def digital_sum(n):
    return sum([int(d) for d in str(n)])


a = b = range(100)

t0 = time()
total1 = max(map(digital_sum, map(lambda (p, q): p**q, it.product(a, b))))
t1 = time()

print '{t}s with functional programming'.format(t=t1 - t0)

t0 = time()
total2 = max([digital_sum(p**q) for p, q in it.product(a, b)])
t1 = time()

print '{t}s with list comprehension'.format(t=t1 - t0)

print total1, total2

