"""Quicksort is an efficient 'divide and conquer' sorting algorithm.

On average, quicksort takes O(n log n) comparisons to sort n items. It's
not a stable sort, meaning that the order of equal elements is not preserved.
Quick sort is memory efficient as it sorts the array 'in place'
(unlike mergesort).

Algorithm steps:
    1. Select a 'pivot' value.
    2. Move the other elements to the appropriate side of the pivot, which
       places the pivot in its correct position.
    3. Repeat steps 1 & 2 with both sides of the list from the pivot until the
       sublists are single element sorted lists.
"""


def quicksort(a_list):
    # Use the first element in the list as the pivot point
    recursive_quicksort(a_list, 0, len(a_list) - 1)


def recursive_quicksort(a_list, pivot_point, right):
    # If the length of the list is 1, then it's already sorted
    if right > pivot_point:
        # Find 'split point' - the pivots correct position.
        split_point = partition(a_list, pivot_point, right)
        # Recursively sort both sides of the list from split point
        recursive_quicksort(a_list, pivot_point, split_point - 1)
        recursive_quicksort(a_list, split_point + 1, right)


def partition(a_list, pivot_point, right):
    left = pivot_point + 1

    # Find elements in list that need to be moved in realtion to the pivot
    while True:
        # Starting from the left stop at a value that is greater than the pivot
        while left <= right and a_list[left] < a_list[pivot_point]:
            left += 1

        # Then from the right stop at a value that is less than the pivot
        while right >= left and a_list[right] > a_list[pivot_point]:
            right -= 1

        # If there are no elements to be moved, 'right' is the pivots position
        if right < left:
            break

        # Move elements to appropriate side of pivot
        a_list[left], a_list[right] = a_list[right], a_list[left]

        # We've just swapped them so no need to compare them again
        left += 1
        right -= 1

    # Put the pivot in its correct place in the list
    a_list[pivot_point], a_list[right] = a_list[right], a_list[pivot_point]

    return right


# Testing
def _assert_sorts_list(test_list):
    """Assert the list has been correctly sorted by the algorithm."""
    sorted_list = sorted(test_list)
    quicksort(test_list)
    assert test_list == sorted_list


_assert_sorts_list([])
_assert_sorts_list([2])
_assert_sorts_list([3, 4])
_assert_sorts_list([2, 4, 5, 3, 6, 1, 100, 80])
_assert_sorts_list([2, -4, -5, 3, -3, 1, -200, 101])
