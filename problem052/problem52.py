#!/usr/bin/env python2
from time import time

t0 = time()
def multiples(x):
    return [ k * x for k in (2, 3, 4, 5, 6)]

def test(x):
    s = set(str(x))
    for n in multiples(x):
        if set(str(n)) != s:
            return False
    return True

for x in range(1, 1000000):
    if test(x):
        print x
        break
        
t1 = time()

print '**Time:**', t1 - t0
