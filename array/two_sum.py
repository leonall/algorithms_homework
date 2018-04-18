#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)

if true, return the first answer
"""

import numpy as np
import unittest

def two_sum(lst, target):
    dic = {}
    for i, num in enumerate(lst):
        if num in dic:
            return [dic[num], i]
        else:
            dic[target - num] = i
    return None


class Test_two_sum(unittest.TestCase):

    def test_two_sum(self):
        lst = range(20)
        for _ in range(10):
            target = np.random.choice(lst)
            res = two_sum(lst, target)
            if res:
                self.assertEqual((lst[res[0]] + lst[res[1]]), target)
            self.assertIsNone(two_sum(lst, -1), None)

if __name__ == '__main__':
    unittest.main()
