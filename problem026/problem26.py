#!/usr/bin/env python2

def divide(d):
    '''
    divide(d): Old school division 1/d.

    Returns an array of digits (quotient) and an array of 
    residuals. Stops when the residual repeats.
    '''
    q, r = 10 / d, 10 % d
    quotients = [q]
    residuals = [r]

    while True:
        r *= 10
        q = r / d
        r %= d
        quotients.append(q)
        if r in residuals:
            residuals.append(r)
            break
        else:
            residuals.append(r)

    return quotients, residuals


def len_cycle(residuals):
    repeated = residuals[-1]
    return len(residuals) - residuals.index(repeated) - 1


def pprint_cycle(quotients, residuals):
    repeated = residuals[-1]
    start_pos = residuals.index(repeated)
    
    precycle = ''.join(map(str, quotients[:start_pos]))
    cycle = ''.join(map(str, quotients[start_pos:]))
    postcycle = str(quotients[start_pos])
    
    return '%s(%s)%s...' % (precycle, cycle, postcycle)


max_d, max_len = 2, 0

for d in xrange(2, 1001):
    new_len = len_cycle(divide(d)[1])
    if new_len > max_len:
        max_len, max_d = new_len, d


print max_d, max_len

#for d in range(50, 100):
#    quot, res = divide(d)
#    print d, 1.0/d, pprint_cycle(quot, res), (quot, res)
