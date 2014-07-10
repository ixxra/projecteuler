#!/usr/bin/env python2

from sympy import isprime
from time import time
import itertools as it

m = [10**k for k in range(6)]
t0 = time()
for p in it.permutations(m):
    #for a, b, c in it.product(range(10), range(10), range(10)):
    for a in range(10):
        for b in range(a, 10):
            for c in range(b, 10):
                s = sum(map(lambda (x, y): x * y, zip((a, b, c, 0, 0, 0), p)))
            #if s > 9999:
                f = filter(isprime, [s + d * p[-1] + d * p[-2] + d * p[-3] for d in range(10)])
                if len(f) > 7 and f[0] > 99999:
                    print a,b, c, p, s, f, len(f)
t1 = time()

print t1 - t0
