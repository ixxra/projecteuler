#!/usr/bin/env python2
import numpy as np
import sympy as sp


def spiral(N=7):
    '''
    Calculates a spiral matrix of `N x N`. It starts in the center
    with a value of `1` and then it fills the matrix counterclockwise,
    up to `N**2` in the bottom-right corner.

    Example:

    This is `spiral(7)`:

    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49
    '''
    if N % 2 == 0:
        raise Exception('Only odd sides allowed!')
    
    S = np.zeros((N,N))
    S[N/2, N/2] = 1

    T = S

    for k in range(N, 2, -2):
        first = (k - 2)**2
        last = k**2
     
        line = np.arange(first + 1,last + 1)
     
        bottom = line[-k:]
        left = line[-2 * k + 1: -k]
        top = list(reversed(line[-3*k + 2:-2*k + 1]))
        right = list(reversed(line[:-3*k + 2]))
     
        T[-1,:] = bottom
        T[:-1, 0] = left
        T[0, 1:] = top
        T[1:-1, -1] = right
     
        T = T[1:-1, 1:-1]

    return S


def corners(step = 7):
    '''
    Calculates the corners in the `N` layer of the Lattice.
    Each `N` layer goes from $N**2$ down to $(N - 1)**2$ + 1$ 
    circling around counterclockwise.


    In spiral(7):

    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49


    corners(7) would be (31, 37, 43, 49).
    '''
    if step % 2 == 0:
        raise Exception('Only odd steps allowed')

    bottom_right = step**2
    bottom_left = bottom_right - step + 1
    top_left = bottom_left - step + 1
    top_right = top_left - step + 1

    return (top_right, top_left, bottom_left, bottom_right)


N = 3
prime_count = len(filter(sp.isprime, corners(N)))
total = 2 * N - 1
ratio = prime_count / float(total)

print N, ratio

while ratio >= 0.10:
    N += 2
    total += 4
    prime_count += len(filter(sp.isprime, corners(N)))
    ratio = prime_count / float(total)
    print N, ratio




