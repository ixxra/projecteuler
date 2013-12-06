#!/usr/bin/env python2
from math import sqrt


N = 600851475143


def is_prime(x):
    for i in xrange(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


def factor(x):
    for p in  xrange(2, int(sqrt(x) + 1)):
        if N % p == 0:
            return N / p


oldN = N


while not is_prime(N):
    N = factor(N)


print 'Biggest prime factor of %d: %d' % (oldN, N)
