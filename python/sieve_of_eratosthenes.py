#!/usr/bin/env python
"""Sieve of Eratosthenes algorithm

Find all the prime numbers less than or equal to a given integer n
"""


def sieve(n):
    crossed = set()
    # Start from the smallest prime numer 2 to n
    for p in xrange(2, n):
        # Iterate over non crossed out numbers
        if p in crossed:
            continue
        # Break if every pth number is crossed out already
        if p * p > n:
            break
        # Cross out all numbers from 2p in steps of p (i.e. multiples of p)
        for i in xrange(p * 2, n, p):
            crossed.add(i)

    # Return non crossed out numbers (prime numbers)
    return set(xrange(2, n)) - crossed


# Test
assert set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]) == sieve(45)
