# -*- coding: utf-8 -*-
"""Bubblesort simple sorting algorithm.

Bubble sort has a worst and average complexity of O(n²).
"""


def bubble_sort(sequence):
    unsorted = True
    # loop until we make one pass with no swaps
    while unsorted:
        unsorted = False
        # iterate from index 0 -> 2nd last item in list as comparing with i + 1
        for i in range(len(sequence) - 1):
            if sequence[i] > sequence[i + 1]:
                unsorted = True  # swap took place, will need to iterate again
                # Swap in one line, no need for temp variable
                sequence[i + 1], sequence[i] = sequence[i], sequence[i + 1]
