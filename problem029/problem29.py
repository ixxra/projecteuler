#!/usr/bin/env python2

seq = set([a**b for a in xrange(2, 101) for b in xrange(2, 101)])

print len(seq)
