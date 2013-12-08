#!/usr/bin/env python2


def is_pythagorean(a, b, c):
    return a**2 + b**2 == c**2


for c in range(334, 999):
    for b in xrange(int((1000 - c) / 2 - 1), c):
        a = 1000 - b - c
        if is_pythagorean(a, b, c):
            print a * b * c
            exit(0)
