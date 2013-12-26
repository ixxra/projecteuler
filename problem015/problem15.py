#!/usr/bin/env python2
from operator import mul
from math import factorial


N, M = 20, 20


print reduce(mul, xrange(21, 41)) / factorial(20)


# N = 2
# M = 2

# def paths(n, m):
#     if n == N or m == M:
#         return 1
#     else:
#         total = 0
#         for i in xrange(n + 1, N + 1):
#             for j in xrange(m + 1, M + 1):
#                 total += paths(i, j)
#         return total


# print paths(0, 0)
