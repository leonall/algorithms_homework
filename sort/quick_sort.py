#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Quick Sort
    ----------
    Uses partitioning to recursively divide and sort the list
    Stable: No
    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.
    https://github.com/qiwsir/algorithm/blob/master/quick_sort.md
"""

import numpy as np
import unittest

def quick_sort(seq):
    '''
    Time Complexity: O(nlog(n)) avrage, O(n**2) worst case
    Space Complexity: O(n**2) this version
    '''
    if len(seq) <= 1:
        return seq
    pivot = seq[0]
    left, right = [], []
    for x in seq[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)


def quick_sort2(seq):
    '''
    Time Complexity: O(nlog(n)) avrage, O(n**2) worst case
    Space Complexity: O(nlog(n)) this version
    '''
    if len(seq) <= 1:
        return seq
    pivot = seq[0]
    left, right = [], []
    middle = [pivot]
    for x in seq[1:]:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)
    return quick_sort(left) + middle + quick_sort(right)


class Test_bubble_sort(unittest.TestCase):

    def test_quick_sort(self):
        for _ in range(10):
            arr = np.random.randint(0, 100, 20).tolist()
            sorted_arr = sorted(arr)
            self.assertEqual(quick_sort(arr), sorted_arr)
            self.assertEqual(quick_sort(sorted_arr), sorted_arr)

    def test_quick_sort2(self):
        for _ in range(10):
            arr = np.random.randint(0, 100, 20).tolist()
            sorted_arr = sorted(arr)
            self.assertEqual(quick_sort2(arr), sorted_arr)
            self.assertEqual(quick_sort2(sorted_arr), sorted_arr)

if __name__ == '__main__':
    unittest.main()
