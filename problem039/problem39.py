#!/usr/bin/env python2

def is_rectangle(a, b, c):
    return a**2 + b**2 == c**2


max_sols, max_p = 0, 0

for p in xrange(3, 1001):
    solutions = 0

    for a in xrange(1, p - 1):
        for b in xrange(a, p):
            c = p - a - b
            
            if c < b:
                break

            if is_rectangle(a, b, c):
                solutions += 1
            
    if solutions > max_sols:
        max_sols, max_p = solutions, p


print max_p
