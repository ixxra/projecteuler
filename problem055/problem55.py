#!/usr/bin/env python2
from time import time


def is_lychrel(x):
    y = int(''.join(reversed(list(str(x)))))
    x += y
    for k in range(49):
        y = int(''.join(reversed(list(str(x)))))
        if x == y:
            return False
        x += y
    return True


t0 = time()
print reduce(lambda s1, s2: s1 + s2, map(is_lychrel, xrange(10000)))
t1 = time()

print '{t}s'.format(t=t1 - t0)
