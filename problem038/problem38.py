#!/usr/bin/env python2
from itertools import permutations
from math import ceil


digits = map(str, range(1, 10))

def concatenate(number, tuple):
    return ''.join(map(lambda d: str(number * d), tuple))


def is_pandigital(n):
    digits = str(n)

    if '0' in digits:
        return False
    
    return len(set(digits)) == 9 and len(digits) == 9


big = 0

for n in xrange(2, 9):
    R = int(ceil(9.0 / n))
    t = range(1, n + 1)
    for r in range(1, R + 1):
        for d in map(lambda p: int(''.join(p)), permutations(digits, r)):
            c = concatenate(d, t)

            if is_pandigital(c) and c > big:
                big = c


print big
