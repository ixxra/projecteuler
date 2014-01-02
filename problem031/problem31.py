#!/usr/bin/env python2
from itertools import product
from operator import mul


total = 1 #One 200 pound coin

for n1 in (0, 100, 200):
    
    for n2 in (0, 50, 100, 150, 200):
        
        if n1 + n2 > 200:
            break

        for n3 in xrange(0, 201, 20):

            if n1 + n2 + n3 > 200:
                break

            for n4 in xrange(0, 201, 10):

                if n1 + n2 + n3 + n4 > 200:
                    break

                for n5 in xrange(0, 201, 5):

                    if n1 + n2 + n3 + n4 + n5 > 200:
                        break

                    for n6 in xrange(0, 201, 2):

                        if n1 + n2 + n3 + n4 + n5 + n6 > 200:
                            break                         
                        #print (n1, n2, n3, n4, n5, n6)
                        total += 1

print total
