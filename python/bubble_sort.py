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


# Testing
def _assert_sorts_list(test_list):
    """Assert the list has been correctly sorted by the algorithm."""
    sorted_list = sorted(test_list)
    bubble_sort(test_list)
    assert test_list == sorted_list


_assert_sorts_list([])
_assert_sorts_list([2])
_assert_sorts_list([3, 4])
_assert_sorts_list([2, 4, 5, 3, 6, 1, 100, 80])
_assert_sorts_list([2, -4, -5, 3, -3, 1, -200, 101])
