#!/usr/bin/env python2

from sympy import isprime
from time import time

t0 = time()
primes = [p for p in xrange(3, 1000000, 2) if isprime(p)]
primes.insert(0, 2)

count = 21
big_prime = -1

for k in xrange(count, len(primes), 2):
    ss = primes[:k+1]
    s = sum(ss)
    l = len(ss)
    
    if s > 1000000:
        break
    
    if s in primes and l > count:
        count = l
        big_prime = s
        
if count % 2 == 0:
    count += 1
    

for i in xrange(3, len(primes) - count, 2):
    for k in xrange(i + count - 1, len(primes) - count, 2):
        ss = primes[i:k+1]
        s = sum(ss)
        l = len(ss)
        
        if s > 1000000:
            break
            
        if s in primes and l > count:
            count = l
            big_prime = s


print big_prime, l
t1 = time()

print t1 - t0
