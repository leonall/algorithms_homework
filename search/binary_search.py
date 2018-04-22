#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    binary search
    -----------
    Binary search works for a sorted array.
    Time Complexity: O(log(n))
    Space Complexity: O(n)
    Stable: Yes
    https://github.com/qiwsir/algorithm/blob/master/bin_search.md
"""

import numpy as np
import unittest

def binary_search(ls, query):
    ls = sorted(ls)
    imin = 0
    imax = len(ls) - 1
    while imax >= imin:
        mid = (imax + imin) // 2
        var = ls[mid]
        if var == query:
            return mid
        elif var > query:
            imax = mid -1
        else:
            imin = mid +1
    return False


if __name__ == '__main__':

    class Test_bubble_sort(unittest.TestCase):

        def test_binary_search(self):
            for _ in range(10):
                arr = range(20)
                i = np.random.choice(range(20))
                self.assertEqual(binary_search(arr, arr[i]), i)
                self.assertFalse(binary_search(arr, -1), False)

        def test_binary_search2(self):
            for _ in range(10):
                arr = sorted(np.random.randint(0, 10, 20).tolist())  # maybe duplicated number,
                var = np.random.choice(range(10))                    # binary search can't be sure the first occurance one
                if var in arr:
                    self.assertEqual(arr[binary_search(arr, var)], var)
                else:
                    self.assertFalse(binary_search(arr, var), False)

    unittest.main()
