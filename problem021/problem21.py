#!/usr/bin/env python2


def d(n):
    total = 1
    for i in xrange(2, n/2 + 1):
        if n % i == 0:
            total += i
    return total


total_amicables = 0

for i in xrange(4, 10001):
    j = d(i)

    if j <= i:
        continue
    
    if d(j) == i: #We found amicable numbers
        total_amicables += i + j


print total_amicables 
