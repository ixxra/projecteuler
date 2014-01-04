#!/usr/bin/env python2
from math import sqrt


def istriangle(t):
    n = (-1 + sqrt(1 + 8 * t)) / 2.0
    return n == int(n)


def ispentagonal(p):
    n = (1 + sqrt(1 + 24*p)) / 6.0
    return n == int(n)


def ishexagonal(h):
    n = (1 + sqrt(1 + 8*h)) / 4.0

    return n == int(n)

n = 286
while True:
    i = n * (n + 1) / 2
    if ispentagonal(i) and ishexagonal(i):
        print i
        exit(0)
    n += 1

