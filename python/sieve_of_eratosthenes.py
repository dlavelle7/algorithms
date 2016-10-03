#!/usr/bin/env python
"""Sieve of Eratosthenes algorithm

Find all the prime numbers less than or equal to a given integer n
"""
import sys


def sieve(num):
    crossed = set()
    # Start at the smallest prime 2
    for p in xrange(2, num):
        # Iterate on non crossed out numbers
        if p in crossed:
            continue
        # Cross out all numbers from 2p in steps of p
        found = False
        for i in xrange(p * 2, num, p):
            crossed.add(i)
            found = True
        # Keep crossing out until we get a clean pass
        if not found:
            break

    return set(xrange(2, num)) - crossed


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "You must pass exactly one argument to this script."
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print "You must pass an integer argument to this script."
        sys.exit(1)
    else:
        sieve(n)


# Tests
assert set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == sieve(30)
