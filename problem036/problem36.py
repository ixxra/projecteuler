#!/usr/bin/env python2

def double_palindrome(n):
    dec_n = str(n)

    for d1, d2 in zip(dec_n, reversed(dec_n)):
        if d1 != d2:
            return False

    bin_n = bin(n)[2:]
    
    for b1, b2 in zip(bin_n, reversed(bin_n)):
        if b1 != b2:
            return False

    return True


print sum(filter(double_palindrome, xrange(10**6)))
