#!/usr/bin/env python2
from math import factorial


def digits(n):
    return map(int, str(n))


def factorial_sum(n):
    return sum(map(factorial, digits(n)))


total = 0
for i in range(100, 10**6):
    if i == factorial_sum(i):
        total += i


print total

