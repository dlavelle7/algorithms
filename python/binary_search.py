#!/usr/bin/env python
"""Binary search algorithm.

Finds the position of a given target in a sorted array.
Binary search has a worst case and average performance of O(log n).
Efficient for searching large datasets.

Algorithm steps:
 1 compare the middle value of the list with the target
 2 discard the half of the list where the target cannot be
 3 repeat steps 1 & 2 until the middle value equals the target or not
"""


def binary_search(number, sorted_list):
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = (right + left) // 2  # floor division
        if sorted_list[mid] == number:
            return number
        elif number < sorted_list[mid]:
            right = mid - 1
        else:
            left = mid + 1


if __name__ == "__main__":
    assert binary_search(4, [0, 1, 3, 4]) == 4
    assert binary_search(3, [1, 3, 4]) == 3
    assert binary_search(6, [1, 3, 4]) is None
    assert binary_search(-2, [-3, -2]) == -2
    assert binary_search(6, [6]) == 6
    assert binary_search(6, []) is None
