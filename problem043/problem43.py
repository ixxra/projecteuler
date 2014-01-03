#!/usr/bin/env python2
from itertools import permutations


def pandigital():
    digits = map(str, range(10))
    for p in permutations(digits, 10):
        if p[0] == '0':
            continue

        yield p


def is_divisible(p):
    res = True
    for i, div in enumerate((2, 3, 5, 7, 11, 13, 17)):
        if int(''.join((p[i + 1], p[i + 2], p[i + 3]))) % div != 0:
            res = False
            break

    return res


total = 0
for p in pandigital():
    if is_divisible(p):
        total += int(''.join(p))

print total
