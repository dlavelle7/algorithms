#!/usr/bin/env python


def bubble_sort(sequence):
    unsorted = True
    # loop until we make one pass with no swaps
    while unsorted:
        unsorted = False
        # iterate from index 0 -> 2nd last item in list as comparing with i + 1
        for i in range(len(sequence) - 1):
            if sequence[i] > sequence[i + 1]:
                unsorted = True  # swap took place, need to iterate again
                # Swap in one line, no need for temp variable
                sequence[i + 1], sequence[i] = sequence[i], sequence[i + 1]
    return sequence


if __name__ == "__main__":
    # Test cases (Note: sorted() returns a new list)
    test_list = []
    assert sorted(test_list) == bubble_sort(test_list)
    test_list = [2]
    assert sorted(test_list) == bubble_sort(test_list)
    test_list = [3, 4]
    assert sorted(test_list) == bubble_sort(test_list)
    test_list = [2, 4, 5, 3, 6, 1]
    assert sorted(test_list) == bubble_sort(test_list)
    test_list = [2, 4, 5, 3, 2, 1]
    assert sorted(test_list) == bubble_sort(test_list)
    test_list = [2, -4, -5, 3, -3, 1]
    assert sorted(test_list) == bubble_sort(test_list)
