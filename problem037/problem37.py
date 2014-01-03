#!/usr/bin/env python2
from math import sqrt, ceil


def isprime(n):
    if n == 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for d in xrange(3, int(ceil(sqrt(n))) + 1, 2):
        if n % d == 0:
            return False

    return True


def is_truncatable(n):
    if not isprime(n):
        return False

    digits = str(n)
    total_digits = len(digits)

    for i in range(total_digits):
        if not isprime(int(''.join(digits[i:]))):
            return False
        
        if not isprime(int(''.join(digits[:total_digits - i]))):
            return False

    return True
    

total = 0
count = 0
number = 11

while count < 11:
    if is_truncatable(number):
        total += number
        count += 1

    number += 2


print total
