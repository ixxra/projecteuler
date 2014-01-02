#!/usr/bin/env python2


def gcd(n, d):
    r = d % n

    while r > 0:
        d, n, r = n, r, d % n

    return n


fractions = set()

for n in range(1, 9):
    for d in range(n + 1, 10):
        for k in range(1, 10):
            if (10*n + k) * d == n * (10*k + d):
                comm_div = gcd(n, d)
                fractions.add((n / comm_div, d / comm_div))


n, d = reduce(lambda (n1, d1), (n2, d2): (n1*n2, d1*d2), fractions)

print d / gcd(n, d)
