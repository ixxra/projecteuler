#!/usr/bin/env python2
from math import sqrt
from collections import OrderedDict


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def isprime(x):
    for p in primes:
        if p > sqrt(x):
            break

        if x % p == 0:
            return False
   
    return True


def generate_primes():
    for i in xrange(33, 10000, 2):
        if isprime(i):
            primes.append(i)


generate_primes()


search_space = [(p, set(str(p))) for p in primes]


def test_seq(start, delta):
    blueprint = search_space[start]

    for k in (1, 2):
        target = start + k * delta
        
        if not target in search_space:
            return False

        if search_space[target] != blueprint:
            return False

    return True


start = primes.index(1487) + 1
search_space = search_space[start + 1:]

for idx, t in enumerate(search_space):
    p, v = t
    
    if p < 1000:
        continue

    if p == 1487:
        print 'bad number'
        continue

    for p2, v2 in search_space[idx + 1:]:
        if v2 != v:
            continue

        arit = p2 - p
        p3 = p2 + arit
        
        if not p3 in primes:
            continue

        if set(str(p3)) == v:
            print '%d%d%d' % (p, p2, p3)
            exit(0)
