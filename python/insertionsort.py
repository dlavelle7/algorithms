"""Insertion Sort: simple sorting algorithm.

Insertion sort has a worst case and average performance of O(n²). Insertion
sort is a stable sort, meaning it preserves the order of equal elements and
it sorts the given list in place.

Algorithm steps:
 - iterate over each element in list, creating a sorted sub list behind
 - start at index 1, as one element sublist at index 0 is already sorted
 - at each iteration, copy out the element at the current (outer) index
 - loop backwards over the sub list, moving greater items to the right,
   until you find an element less than the current item
 - insert the current element into the space created
"""


def insertion_sort(a_list):
    # starting at index 1 (as sublist to left, one item, is already sorted)
    for idx in range(1, len(a_list)):
        # copy out current value from the list, until you find it a home
        current_value = a_list[idx]
        position = idx
        # check each item in the already sorted sub list to the left
        while position > 0 and current_value < a_list[position - 1]:
            # move great value over to right
            a_list[position] = a_list[position - 1]
            position -= 1
        # position found for current value, stick it back in
        a_list[position] = current_value


test_list = [5, 1, 3, 4, 2]
insertion_sort(test_list)
print(test_list)
