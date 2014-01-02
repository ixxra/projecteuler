#!/usr/bin/env python2
from math import ceil, sqrt
from itertools import product


def isprime(p):
    if p % 2 == 0:
        return False

    for d in xrange(3, int(ceil(sqrt(p))) + 1, 2):
        if p % d == 0:
            return False
    return True


def count_primes_generated(a, b):
    if not isprime(abs(b)):
        return 0

    pol = lambda n: n**2 + a * n + b
    
    count = 1
    n = 1

    while isprime(abs(pol(n))):
        count += 1
        n += 1
    
    return count


prod = 0
max_primes = 0

for a, b in product(xrange(-999, 1000), xrange(-999, 1000, 2)):
    total_primes = count_primes_generated(a, b)
    if total_primes > max_primes:
        max_primes, prod = total_primes, a * b


for a in xrange(-999, 1000):
    total_primes = count_primes_generated(a, 2)
    if total_primes > max_primes:
        max_primes, prod = total_primes, a * b


print prod 
