#!/usr/bin/env python2

last = 1
total = 1
delta = 2

while last < 1002001:
    for i in range(4):
        last += delta
        total += last
        
    delta += 2


print total
