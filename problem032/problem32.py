#!/usr/bin/env python2
import itertools as it
from time import time


permutations = it.permutations(map(str, range(1, 10)))

total = set()
t1 = time()
for d in permutations:
    for i in range(1, 8):
        for j in range(i+1, 9):
            d1 = int(''.join(d[:i]))
            d2 = int(''.join(d[i:j]))
            d3 = int(''.join(d[j:]))
            if d1*d2 == d3:
                print '%2d x %2d = %2d' % (d1, d2, d3)
                total.add(d3)
t2 = time()

print sum(total)
print t2 - t1, 'seg'
