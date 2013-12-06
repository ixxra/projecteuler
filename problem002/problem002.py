#!/usr/bin/env python2

a = 1
b = 2

sum = 0

while b < 4000001:
    if b % 2 == 0:
        sum += b
    a, b = b, a + b

print sum
