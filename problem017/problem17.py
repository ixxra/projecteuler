#!/usr/bin/env python2
import itertools as it


total = 0

numbers = [
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'then',
        'eleven',
        'twelve',
        'thirteen',
        'fourtheen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eighteen',
        'nineteen']

total += sum(map(len, numbers))

digits = [ 
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine']

tenths = [ 
        'twenty',
        'thirty',
        'fourty',
        'fifty',
        'sixty',
        'seventy',
        'eigthy',
        'ninety']

for number in it.product(tenths, digits):
    print '%s-%s' % number

total += sum(map(len, digits)) * sum(map(len, tenths)) + sum(map(len, tenths))

for number in it.product(digits, tenths, digits):
    print '%s hundred and %s-%s' % number

print total
