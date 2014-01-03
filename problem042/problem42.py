#!/usr/bin/env python2
import re
from math import sqrt


A = ord('A') - 1

def value(word):
    return sum(map(lambda l: ord(l) - A,word))


def is_triangular(t):
    n = (-1 + sqrt(1 + 8*t))/2.0
    return int(n) == n


f = open('words.txt')
total = 0

for word in re.findall(r'\w+', f.read()):
    if is_triangular(value(word)):
        total += 1

print total
