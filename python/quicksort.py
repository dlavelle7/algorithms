"""Quicksort is an efficient 'divide and conquer' sorting algorithm."""


def quicksort(sortable):
    # Lets arbitrarily select the first element in the list as the 'pivot'
    pivot_point = 0
    # Find 'split point' - the pivots correct position
    split_point = partition(sortable, pivot_point)
    # Put the pivot in its correct place in the list
    sortable[pivot_point], sortable[split_point] = sortable[split_point], sortable[pivot_point]
    # TODO: Recursively sort both lists from split point

# TODO
#def recursive_sort():
#    quicksort(list_one)
#    quicksort(list_two)


def partition(sortable, pivot_point):
    left = pivot_point + 1
    right = len(sortable) -1

    # Find elements in list that need to be moved in realtion to the pivot
    while True:
        # Starting from the left stop at a value that is greater than the pivot
        while sortable[left] < sortable[pivot_point]:
            left += 1

        # Then from the right stop at a value that is less than the pivot
        while sortable[right] > sortable[pivot_point]:
            right -= 1

        if right < left:
            return right

        # Swap left and right
        sortable[left], sortable[right] = sortable[right], sortable[left]

        # We've just swapped them so no need to compare them again
        left += 1
        right -= 1



# Testing
sortable = [54, 26, 93, 17, 77, 31, 44, 55, 20]

quicksort(sortable)
