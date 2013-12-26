#!/usr/bin/env python2


def divisors(n):
    _divisors = [1]

    for i in range(2, n/2 + 1):
        if n % i == 0:
            _divisors.append(i)
    _divisors.append(n)

    return _divisors


def count_divisors(n):
    count = 0
    for i in range(2, n/2 + 1):
        if n % i == 0:
            count += 1
    return count
        
    
n = 1
prev_divs = 1
total_divs = 1


while total_divs < 499:
    n += 1
    divs = count_divisors(n + 1)
    total_divs = prev_divs + divs
    prev_divs = divs
    print n, total_divs
    

