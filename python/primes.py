#!/usr/bin/env python
"""Prime numbers.

Find all the prime numbers less than or equal to a given integer n.

A prime number is a whole number greater than 1, whose only factors are 1 and
itself. A factor is a whole number that can be evenly divided into another
number.

See sieve_of_eratosthenes.py for more prime number algorithms.
"""


def simple_primes(n):
    """Basic prime number algorithm."""
    primes = set()
    for i in xrange(2, n + 1):
        # check for factors of i from all the numbers between 2 and i
        for j in xrange(2, i):
            if i % j == 0:
                break
        else:
            primes.add(i)
    return primes


def simple_primes_2(n):
    """Optimization, only check for primes up to half of i.

    e.g. Find the factors of 10:
    - only check from 2 -> 5, no more divisors of 10 after 5 with modulus 0.
    """
    primes = set()
    for i in xrange(2, n + 1):
        j = 2
        top = i // 2  # if j > i/2 you will never get modulus 0 (e.g. 10 / 6)
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
