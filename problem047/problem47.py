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


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def four_divisors(n):
    count = 0
    for p in primes:
        if n % p == 0:
            count += 1

    return count == 4


n = 32
while True:
    if isprime(n):
        primes.append(n)
        n += 1
        
    else:
        found = True
        for x in (n, n + 1, n + 2, n + 3):
            if not four_divisors(x):
                found = False
                n = x + 1
                break

        if found:
            print n
            break

