#!/usr/bin/env python
"""Prime number generator.

Input:
The input begins with the number t of test cases in a single line (t<=10). In
each of the next t lines there are two numbers m and n (1 <= m <= n <=
1000000000, n-m<=100000) separated by a space.

Output
For every test case print all prime numbers p such that m <= p <= n, one number
per line, test cases separated by an empty line.
"""
import sys
import time


def sieve(end):
    # FIXME: Given the max size of m <= 1bln, this is too much memory
    uncrossed = [True for i in xrange(end + 1)]
    uncrossed[0] = uncrossed[1] = False
    for p in xrange(2, end + 1):
        if p * p > end:
            break
        if uncrossed[p]:
            for i in xrange(p**2, end + 1, p):
                uncrossed[i] = False
    return uncrossed


if __name__ == "__main__":
    start = time.time()  # TODO: Remove XXX
    no_of_tcs = int(sys.stdin.readline())
    # Find the biggest n
    ns = set()
    test_cases = []
    for tc in xrange(no_of_tcs):
        m, n = sys.stdin.readline().split()
        ns.add(int(n))
        test_cases.append((int(m), int(n)))
    big_n = max(ns)

    # Create a sieve from 2 to big_n
    master_sieve = sieve(big_n)

    # For each test case range, find primes using master sieve
    for m, n in test_cases:
        for num in xrange(m, n + 1):
            if master_sieve[num]:
                print num
        print ""
    end = time.time()  # TODO: Remove XXX
    print "Execution time %s" % (end - start)  # TODO: Remove XXX
