#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Bubble Sort
    -----------
    A naive sorting that compares and swaps adjacent elements.
    Time Complexity: O(n**2)
    Space Complexity: O(1) Auxiliary
    Stable: Yes
    Psuedo code: http://en.wikipedia.org/wiki/Bubble_sort
"""

import numpy as np
import unittest

def bubble_sort(seq):
    L = len(seq)
    for i in range(L):
        for j in range(1, L-i):
            if seq[j] < seq[j-1]:
                seq[j], seq[j-1] = seq[j-1], seq[j]
    return seq


class Test_bubble_sort(unittest.TestCase):

    def test_bubble_sort(self):
        for _ in range(10):
            arr = np.random.randint(0, 100, 20).tolist()
            sorted_arr = sorted(arr)
            self.assertEqual(bubble_sort(arr), sorted_arr)
            self.assertEqual(bubble_sort(sorted_arr), sorted_arr)


if __name__ == '__main__':

    unittest.main()
