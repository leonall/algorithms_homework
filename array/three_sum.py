#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an array S of n integers, are there elements a, b, c in S
such that a + b + c = target?
Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4], target = 0,
A solution set is:
(-1, 0, 1)

https://github.com/keon/algorithms/blob/master/array/three_sum.py#L11
"""

import unittest
import numpy as np
from two_sum import two_sum

def three_sum(lst, target):
    """
    :param array: List[int]
    :return: Set[ Tuple[int, int, int] ]
    """
    for i, num in enumerate(lst):
        _target = target - num
        _lst = lst[:i] + lst[i+1:]
        res = two_sum(_lst, _target)
        if res:
            return (i, res[0]+1, res[1]+1)
    return None


class Test_three_sum(unittest.TestCase):

    def test_three_sum(self):
        lst = range(20)
        for _ in range(10):
            target = np.random.choice(lst)
            res = three_sum(lst, target)
            if res:
                self.assertEqual((lst[res[0]] + lst[res[1]] + lst[res[2]]), target)
            self.assertIsNone(three_sum(lst, -1), None)


if __name__ == '__main__':

    unittest.main()
