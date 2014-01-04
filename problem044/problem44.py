#!/usr/bin/env python2
from numpy import zeros

pentagonals = [n*(3*n - 1)/2 for n in xrange(1, 2500)]
Max_pent = pentagonals[-1]

z = zeros(2 * Max_pent + 1, dtype='int8')
z[pentagonals] = 1


for i in xrange(len(pentagonals) - 1):
    for j in xrange(i + 1, len(pentagonals)):
        p, q = pentagonals[i], pentagonals[j]
        if z[p + q] == 1 and z[q - p] == 1:
            print q - p
            exit(0)


#s = p + q
        
#        if s > Max_pent:
#            break

#        if s in pentagonals and (q - p) in pentagonals:
#            print (p, q)
#            exit(0)
        
