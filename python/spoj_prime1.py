#!/usr/bin/env python
import sys


def sieve_range(start, end):
    if start < 2:
        start = 2
    uncrossed = [True for i in xrange(end + 1)]
    for p in xrange(2, end + 1):
        if p * p > end:
            break
        if uncrossed[p]:
            for i in xrange(p**2, end + 1, p):
                uncrossed[i] = False

    for num in xrange(start, end + 1):
        if uncrossed[num]:
            print num


if __name__ == "__main__":
    no_of_tcs = int(sys.stdin.readline())
    for tc in xrange(no_of_tcs):
        ranges = sys.stdin.readline().split()
        sieve_range(int(ranges[0]), int(ranges[1]))
        print ""
