#!/usr/bin/env python2
import itertools as it


def sum_of_divisors(n):
    '''
    sum of proper divisors of n
    '''
    initial_n = n
    sum = 1
    p = 2
    while p*p <= n and n > 1:
        if n % p == 0:
            j = p * p
            n = n / p
            while n % p == 0:
                j = j * p
                n = n / p
            sum = sum * (j - 1)
            sum = sum / (p - 1)
        if p == 2: 
            p = 3 
        else: 
            p = p + 2
    if n > 1:
        sum = sum * (n + 1)
    return sum - initial_n


def is_abundant(n):
    return n < sum_of_divisors(n)


abundants = [n for n in xrange(12, 28124) if is_abundant(n)]
totals = range(28124)

for i in xrange(len(abundants)):
    for j in xrange(i, len(abundants)):
        s = abundants[i] + abundants[j]
        if s < 28124:
            totals[s] = 0


print sum(totals)
