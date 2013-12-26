#!/usr/bin/env python2
from sys import argv


digits = lambda n: map(int, str(n))


print sum(digits(2**1000))
