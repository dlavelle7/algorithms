from unittest import TestCase

from python.bubble_sort import bubble_sort
from python.insertion_sort import insertion_sort
from python.quick_sort import quick_sort


class TestSorts(TestCase):

    def setUp(self):
        # Unsorted lists to test against
        self.test_cases = [
            [],
            [2],
            [3, 4],
            [2, 4, 5, 3, 6, 1, 100, 80],
            [2, -4, -5, 3, -3, 1, -200, 101],
            [0, 0, -1, -0.507, 3, 2, 3, 5, 99, 98, 97, 99, 0, -0.5066],
        ]

    def _assert_sorts_in_place(self, algorithm, test_list):
        """Assert the list has been sorted in place by the algorithm."""
        sorted_list = sorted(test_list)
        algorithm(test_list)
        self.assertListEqual(sorted_list, test_list)

    def test_bubble_sort(self):
        for test_list in self.test_cases:
            self._assert_sorts_in_place(bubble_sort, test_list)

    def test_insertion_sort(self):
        for test_list in self.test_cases:
            self._assert_sorts_in_place(insertion_sort, test_list)

    def test_quick_sort(self):
        for test_list in self.test_cases:
            self._assert_sorts_in_place(quick_sort, test_list)
