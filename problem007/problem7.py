#!/usr/bin/env python2


cribe = []
marker = 2


def is_prime(x):
    for n in cribe:
        if x % n == 0:
            return False
    return True


while len(cribe) < 10001:
    if is_prime(marker):
        cribe.append(marker)
    marker += 1


print cribe[-1]
