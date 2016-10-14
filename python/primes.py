#!/usr/bin/env python
"""Prime numbers.

Find all the prime numbers less than or equal to a given integer n.
See sieve_of_eratosthenes.py for more prime number algorithms.
"""
import time

# TODO: Tidy up

def time_me(prime_func):
    def wrapped_func(*args):
        start = time.time()
        primes = prime_func(*args)
        end = time.time()
        print "Execution time of %s is %s" % (prime_func.__name__, start - end)
        return primes
    return wrapped_func


@time_me
def simple_primes(n):
    primes = set()
    for i in xrange(2, n + 1):
        for j in xrange(2, i):
            if i % j == 0:
                break
        else:
            primes.add(i)
    return primes


@time_me
def better_simple_primes(n):
    # TODO: Caching
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


# TODO: Could import sieves here???
# Test execution times
#simple_primes(50000)
#better_simple_primes(50000)
#sieve(1000000)
#optimized_sieve(1000000)

## Test simple_primes
#assert set([2]) == simple_primes(2)
#assert set([2, 3, 5, 7, 11, 13, 17, 19, 23]) == simple_primes(23)
#assert set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == simple_primes(30)

## Test better_simple_primes
#assert set([2]) == better_simple_primes(2)
#assert set([2, 3, 5, 7, 11, 13, 17, 19, 23]) == better_simple_primes(23)
#assert set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == better_simple_primes(30)

# Test sieve
#assert set([2]) == sieve(2)
#assert set([2, 3, 5, 7, 11, 13, 17, 19, 23]) == sieve(23)
#assert set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == sieve(30)

## Test optimized sieve
#assert set([2]) == optimized_sieve(2)
#assert set([2, 3, 5, 7, 11, 13, 17, 19, 23]) == optimized_sieve(23)
#assert set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == optimized_sieve(30)
