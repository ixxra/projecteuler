#!/usr/bin/env python2

def digits(n):
    return map(int, str(n))


total = 0
for n in xrange(2, 1000000):
    if n == sum([d**5 for d in digits(n)]):
        total += n


print total
