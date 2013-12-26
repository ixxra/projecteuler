#!/usr/bin/env python2

def sequence(n):
    _seq = [n]
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        _seq.append(n)
    return _seq


longest  = []
maxcount =  0


for n in range(500000, 1000001):
   if n in longest:
       pass
   else:
       seq = sequence(n)
       if len(seq) > maxcount:
           longest = seq
           maxcount = len(seq)


print 'Result:', longest[0], maxcount
