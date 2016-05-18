#!/usr/bin/env python

def main():
    sorted_list = range(10)
    assert binary_search(0, sorted_list) == 0
    assert binary_search(9, sorted_list) == 9
    assert binary_search(3, sorted_list) == 3
    assert binary_search(4, sorted_list) == 4
    assert binary_search(5, sorted_list) == 5
    assert binary_search(-1, sorted_list) == None
    sorted_list = range(3)
    assert binary_search(1, sorted_list) == 1

def binary_search(number, sorted_list):
    l = 0
    h = len(sorted_list) - 1
    mid = (h + l) / 2
    while l <= h and sorted_list[mid] != number:
        if number < sorted_list[mid]:
            h = mid - 1
        else:
            l = mid + 1
        mid = (h + l) / 2
    return mid if sorted_list[mid] == number else None

if __name__ == "__main__":
    main()
