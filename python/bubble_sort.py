#!/usr/bin/env python

def main():
    test_list = [2, 4, 5, 3, 6, 1]
    assert bubble_sort(test_list) == sorted(test_list)
    test_list = [2]
    assert bubble_sort(test_list) == sorted(test_list)
    test_list = []
    assert bubble_sort(test_list) == sorted(test_list)
    test_list = [2, 4, 5, 3, 2, 1]
    assert bubble_sort(test_list) == sorted(test_list)
    test_list = [2, -4, -5, 3, -3, 1]
    assert bubble_sort(test_list) == sorted(test_list)

def bubble_sort(sequence):
    unsorted = True
    while unsorted: # loop until we make one pass with no swaps
        unsorted = False
        for i in range(len(sequence) -1):
            if sequence[i] > sequence[i + 1]:
                unsorted = True # swap took place, need to iterate again
                # Swap in one line, no need for temp variable
                sequence[i + 1], sequence[i] = sequence[i], sequence[i + 1]
    return sequence

if __name__ == "__main__":
    main()
