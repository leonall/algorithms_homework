#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    first occurance search, apply binary search
    -----------
    Binary search works for a sorted array.
    Time Complexity: O(log(n))
    Space Complexity: O(n)
    Stable: Yes
    https://github.com/qiwsir/algorithm/blob/master/bin_search.md
"""

import numpy as np
import unittest
from binary_search import binary_search


def first_occurance(ls, query):
    idx = binary_search(ls, query)
    if idx is not False:
        while idx > 0 and ls[idx - 1] == query:
            idx -= 1
    return idx


def first_occurance2(ls, query):
    ls = sorted(ls)
    imin, imax = 0, len(ls) - 1
    while imax >= imin:
        mid = (imax + imin) // 2
        var = ls[mid]
        if imin == imax:
            break
        elif var < query:
            imin = mid + 1
        else:
            imax = mid
    if ls[imin] == query:
        return imin
    else:
        return False


class Test_bubble_sort(unittest.TestCase):

    def setUp(self):
        global first_occurance, first_occurance2
        self.fun1 = first_occurance
        self.fun2 = first_occurance2

    def _test_binary_search(self, first_occurance):
        for _ in range(10):
            arr = sorted(np.random.randint(0, 10, 20).tolist())  # maybe duplicated number,
            var = np.random.choice(range(10))
            if var in arr:
                self.assertEqual(first_occurance(arr, var), arr.index(var))
            else:
                self.assertEqual(binary_search(arr, var), False)
            arr2 = [1] * 10
            self.assertEqual(first_occurance(arr2, 1), 0)
            self.assertEqual(first_occurance(arr2, 0), False)
            self.assertEqual(first_occurance(arr2, 2.5), False)

    def test_binary_search(self):
        self._test_binary_search(self.fun1)

    def test_binary_search2(self):
        self._test_binary_search(self.fun2)

if __name__ == '__main__':
    unittest.main()
