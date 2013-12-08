#!/usr/bin/env python2
MAX = 2000000
numbers = range(2, MAX)


for i, n in enumerate(numbers[:MAX/2]):
    if n != 0:        
        for x in xrange(i + n, MAX - 2, n):
            numbers[x] = 0


print sum(numbers)
