#!/usr/bin/env python

def main():
    true_fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    assert fibonacci(len(true_fib)) == true_fib
    true_fib = [0, 1]
    assert fibonacci(2) == true_fib
    true_fib = [0]
    assert fibonacci(1) == true_fib

def fibonacci(n):
    """Returns a list of fibonacci numbers of length n"""
    sequence = [0, 1]
    if n < len(sequence):
        return sequence[:n]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == "__main__":
    main()
