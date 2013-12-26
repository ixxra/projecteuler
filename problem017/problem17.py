#!/usr/bin/env python2
import itertools as it


total_chars = lambda listing: sum(map(len, listing))
total = 0


total += total_chars([
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
        'nineteen'])


total_digits = total_chars([ 
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine'])


total_tenths = total_chars([ 
        'twenty',
        'thirty',
        'fourty',
        'fifty',
        'sixty',
        'seventy',
        'eigthy',
        'ninety'])

total += total_tenths + total_tenths * total_digits
numbers_less_than_one_hundred = total

total += total_digits * total_chars(['hundred', 'and']) * numbers_less_than_one_hundred
total += total_chars(['one', 'thousand'])
print total
