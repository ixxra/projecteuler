#!/usr/bin/env python2
import sympy as sp

def continued_fraction(n):
    f = sp.Rational(3,2)
    fractions = [f]
    
    for k in range(n):
        f = 1 + 1/(1 + f)
        fractions.append(f)

    return fractions


print len(filter(lambda f: len(str(f.p)) > len(str(f.q)), continued_fraction(1000)))

