#!/usr/bin/env python2

print sum(map(lambda n: n**n % 10**10, xrange(1, 1001))) % 10**10
