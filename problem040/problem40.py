#!/usr/bin/env python2

def seq():
    a = 1
    while True:
        digits = map(int, str(a))

        for d in digits:
            yield d
        
        a += 1


prod = 1
for i, s in  enumerate(seq()):
    if i in (0, 9, 99, 999, 9999, 99999):
        prod *= s

    if i == 999999:
        prod *= s
        break


print prod
