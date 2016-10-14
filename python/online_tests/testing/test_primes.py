#!/usr/bin/env python
"""Prime numbers.

Find all the prime numbers less than or equal to a given integer n
"""
import time


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


@time_me
def sieve(n):
    crossed = set()
    # Start from the smallest prime numer 2 to n
    for p in xrange(2, n + 1):
        # Break if every pth number is crossed out already
        if p * p > n:
            break
        # Iterate over non crossed out numbers
        if p in crossed:
            continue
        # Cross out all numbers from 2p in steps of p (i.e. multiples of p)
        for i in xrange(p * 2, n + 1, p):
            crossed.add(i)

    # Return non crossed out numbers (prime numbers)
    return set(xrange(2, n + 1)) - crossed


@time_me
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


@time_me
def optimized_sieve_2(n):
    # Create a list of bools with indecies from 2 to n, set all true initally
    crossed = [True] * (n + 1)
    # Start from the smallest prime numer 2 to n
    for p in xrange(2, n + 1):
        # If not crossed out already
        if crossed[p]:
            # Start enumerating the multiples of each prime p from p squared
            for i in xrange(p**2, n + 1, p):
                crossed[i] = False

    return set(num for num in xrange(2, n + 1) if crossed[num])


@time_me
def sieve_range(start, end):
    uncrossed = [True] * (end + 1)
    uncrossed[0] = uncrossed[1] = False
    for p in xrange(2, end + 1):
        if p * p > end:
            break
        if uncrossed[p]:
            for i in xrange(p**2, end + 1, p):
                uncrossed[i] = False

    return set(num for num in xrange(start, end + 1) if uncrossed[num])


@time_me
def foo(n):
    crossed = [True for i in xrange(n)]

@time_me
def foo2(n):
    # This is a lot faster
    crossed = [True] * n


#foo(1000000000)
#foo2(1000000000)


# Test execution times
#simple_primes(50000)
#better_simple_primes(50000)
#sieve(1000000)
#optimized_sieve(1000000)
#optimized_sieve_2(1000000)
sieve_range(5000000, 10000000)

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

# Test sieve range
assert set([2]) == sieve_range(2, 2)
assert set([2, 3, 5, 7, 11, 13, 17, 19, 23]) == sieve_range(0, 23)
assert set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == sieve_range(1, 30)
assert set([11, 13, 17, 19, 23, 29]) == sieve_range(11, 29)
assert set([7, 11, 13, 17, 19, 23, 29]) == sieve_range(6, 30)
