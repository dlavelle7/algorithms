#!/usr/bin/env python
"""Prime numbers.

Find all the prime numbers less than or equal to a given integer n.

A prime number is a number greater than 1 that has no positive divisors other
than 1 and itself.

See sieve_of_eratosthenes.py for more prime number algorithms.
"""


def simple_primes(n):
    """Basic prime number algorithm."""
    primes = set()
    for i in xrange(2, n + 1):
        for j in xrange(2, i):
            if i % j == 0:
                break
        else:
            primes.add(i)
    return primes


def simple_primes_2(n):
    primes = set()
    for i in xrange(2, n + 1):
        j = 2
        top = i / 2  # if j > i you will never get modulus 0 (e.g. 30 / 16)
        while j <= top:
            if i % j == 0:
                break
            j += 1
        else:
            primes.add(i)
    return primes


# Test simple_primes
assert set([2]) == simple_primes(2)
assert set([2, 3, 5, 7, 11, 13, 17, 19, 23]) == simple_primes(23)
assert set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == simple_primes(30)

# Test simple_primes_2
assert set([2]) == simple_primes_2(2)
assert set([2, 3, 5, 7, 11, 13, 17, 19, 23]) == simple_primes_2(23)
assert set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == simple_primes_2(30)
