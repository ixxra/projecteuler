#!/usr/bin/env python2

A = ord('A') - 1

def score(name):
    '''
    returns name score.
    @name uppercase string of A-Z characters
    '''
    return sum(map(lambda letter: ord(letter) - A, name))


names = [name[1:-1] for name in open('names.txt').read().split(',')]
names.sort()

print sum(map(lambda (i, name): (i+1)*score(name), enumerate(names)))
