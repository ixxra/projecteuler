#!/usr/bin/env python2
import re


def parse_number(n):
    first_numbers = [
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten',
        'eleven',
        'twelve',
        'thirteen',
        'fourteen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eighteen',
        'nineteen']
    
    digits = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'}
    
    tenths = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eigthy',
        9: 'ninety'}

    if n < 20:
        return first_numbers[n - 1]

    elif n == 1000:
        return 'one thousand'
    
    elif n < 100:
        t, u = n / 10, n % 10
        if u == 0:
            return tenths[t]
        else:
            return '%s-%s' % (tenths[t], digits[u])
    
    else:
        h, m = n / 100, n % 100
        if m == 0:
            return '%s hundred' % digits[h]
        else:
            if m < 20:
                return '%s hundred and %s' % (digits[h], first_numbers[m - 1])
            else:
                t, u = m / 10, m % 10
                if u == 0:
                    return '%s hundred and %s' % (digits[h], tenths[t])
                else:
                    return '%s hundred and %s-%s' % (digits[h], tenths[t], digits[u])


letters = re.compile(r'[a-z]')
total = 0

for i in range(1, 1001):
    total += len(letters.findall(parse_number(i)))
        
print total
