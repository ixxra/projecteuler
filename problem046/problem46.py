#!/usr/bin/env python2
from math import sqrt, ceil


def isprime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for d in xrange(3, int(ceil(sqrt(x))) + 1, 2):
        if x % d == 0:
            return False
    return True


def issquare(n):
    x = sqrt(n)
    return int(x) == x


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def conjecture(n):
    for p in primes:
        if issquare((n - p)/2):
            return True

    return False


n = 35

while True:
    if isprime(n):
        primes.append(n)

    else:
        if not conjecture(n):
            print n
            break

    n += 2
