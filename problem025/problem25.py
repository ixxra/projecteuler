#!/usr/bin/env python2
import numpy as np


MAX_DIGITS = 1001


def bignum():
    return np.zeros(MAX_DIGITS, dtype='int8')


def bignum_sum(num1, num2, num3):
    carry = 0
    for i in range(MAX_DIGITS):
        res = num1[i] + num2[i] + carry
        num3[i] = res % 10
        carry = res / 10


def bignum_digits(num):
    digits = MAX_DIGITS
    for d in reversed(num):
        if d == 0:
            digits -= 1
        else:
            break
    return digits


def bignum_tostr(num):
    d = bignum_digits(num)
    return ''.join(map(str, reversed(num[:d+1])))


f1 = bignum()
f1[0] = 1

f2 = bignum()
f2[0] = 1

f3 = bignum()
bignum_sum(f1, f2, f3)

counter = 3
digits = bignum_digits(f3)

try:
    while digits < 1000:
        f1, f2, f3 = f2, f3, f1
        bignum_sum(f1, f2, f3)

        digits = bignum_digits(f3)
        counter += 1


except:
    print '-- DEBUG ---------------------------'
    print 'counter:', counter
    print 'digits:', digits
    print 'Last fibonacci:', bignum_tostr(f3)


print bignum_tostr(f3)
print counter
