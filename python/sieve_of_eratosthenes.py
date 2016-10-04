#!/usr/bin/env python
"""Sieve of Eratosthenes algorithm

Find all the prime numbers less than or equal to a given integer n
"""


def simple_sieve(n):
    crossed = set()
    # Start from the smallest prime numer 2 to n
    for p in xrange(2, n + 1):
        # Iterate over non crossed out numbers
        if p in crossed:
            continue
        # Cross out all multiples of p, after p
        found = False
        for i in xrange(p * 2, n + 1, p):
            crossed.add(i)
            found = True
        # Break if every pth number is crossed out already
        if not found:
            break

    # Return non crossed out numbers (prime numbers)
    return set(xrange(2, n + 1)) - crossed


def optimized_sieve(n):
    # Create a list of bools with indecies from 2 to n, set all true initally
    crossed = [True for i in xrange(n + 1)]
    # Start from the smallest prime numer 2 to n
    for p in xrange(2, n + 1):
        # If not crossed out already
        if crossed[p]:
            # Start enumerating the multiples of each prime p from p squared
            for i in xrange(p**2, n + 1, p):
                crossed[i] = False

    return set(num for num in xrange(2, n + 1) if crossed[num])


# Test sieve
assert set([2, 3, 5, 7, 11, 13, 17, 19, 23]) == simple_sieve(23)
assert set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == simple_sieve(30)

# Test optimized sieve
assert set([2, 3, 5, 7, 11, 13, 17, 19, 23]) == optimized_sieve(23)
assert set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == optimized_sieve(30)
