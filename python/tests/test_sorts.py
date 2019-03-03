from unittest import TestCase

from python.bubble_sort import bubble_sort
from python.insertion_sort import insertion_sort
from python.quick_sort import quick_sort


class TestSorts(TestCase):

    # Unsorted lists to test against
    test_cases = [
        [],
        [2],
        [3, 4],
        [2, 4, 5, 3, 6, 1, 100, 80],
        [2, -4, -5, 3, -3, 1, -200, 101],
        [0, 0, -1, -0.507, 3, 2, 3, 5, 99, 98, 97, 99, 0, -0.5066],
    ]

    # Algorithms to test (add new ones here)
    test_algorithms = (
        bubble_sort,
        insertion_sort,
        quick_sort,
    )

    def _assert_sorts_in_place(self, algorithm, test_list):
        """Assert the list has been sorted in place by the algorithm."""
        sorted_list = sorted(test_list)
        algorithm(test_list)
        self.assertListEqual(sorted_list, test_list)

    def test_sorting(self):
        for algorithm in self.test_algorithms:
            for test_list in self.test_cases:
                self._assert_sorts_in_place(algorithm, test_list)
