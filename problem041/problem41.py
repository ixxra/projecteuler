#!/usr/bin/env python2
from itertools import permutations
from math import ceil, sqrt


def isprime(p):
    if p == 1:
        return False

    if p == 2:
        return True

    if p % 2 == 0:
        return False

    for d in xrange(3, int(ceil(sqrt(p))) + 1, 2):
        if p % d == 0:
            return False

    return True


digits = map(str, xrange(1, 10))

for r in range(9, 0, -1):
    big = 0
    for p in permutations(digits[:r], r):
        number = int(''.join(p))
        if isprime(number) and number > big:
            big = number

    if big > 0:
        print big
        break

