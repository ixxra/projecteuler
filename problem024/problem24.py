#!/usr/bin/env python2
import itertools as it


p = it.permutations(range(10), 10)

for i, perm in enumerate(p):
    if i == 999999:
        print ''.join(map(str, perm))
        break

