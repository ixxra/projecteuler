#!/usr/bin/env python2
from math import sqrt, ceil


def cyclic_idx(n):
    for l in xrange(n):
        yield [(i + l) % n for i in xrange(n)]


def isprime(n):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for d in xrange(3, int(ceil(sqrt(n))) + 1, 2):
        if n % d == 0:
            return False

    return True


total = 0
for i in range(2, 10**6):
    d = str(i)
    is_cyclic = True

    for perm in cyclic_idx(len(d)):
        n = int(''.join(map(lambda k: d[k], perm)))
        
        if not isprime(n):
            is_cyclic = False
            break

    if is_cyclic:
        total += 1


print total

