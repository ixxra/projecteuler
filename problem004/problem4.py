#!/usr/bin/env python2

def is_palindrome(x):
    x = str(x)
    for w1, w2 in zip(x, reversed(x)):
        if w1 != w2:
            return False
    return True


pal = 0
pal_i = 0
pal_j = 0


for i in range(100, 1001):
    for j in range(i, 1001):
        N = i * j
        if is_palindrome(N):
            if N > pal:
                pal, pal_i, pal_j = N, i, j 
           
print pal, pal_i, pal_j
