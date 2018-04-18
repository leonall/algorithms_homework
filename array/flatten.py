#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
give a single resultant array.
function flatten(input){
}
Example:
Input: var input = [2, 1, [3, [4, 5], 6], 7, [8]];
flatten(input);
Output: [2, 1, 3, 4, 5, 6, 7, 8]
"""

import unittest
import numpy as np


def list_flatten(lst):
    """
    :param lst: List
    :return: List
    """
    ls = []
    for item in lst:
        if not isinstance(item, list) and not isinstance(item, tuple):
            ls.append(item)
        else:
            ls.extend(list_flatten(item))
    return ls


class Test_list_flatten(unittest.TestCase):

    def test_list_flatten(self):
        lst = np.arange(6).reshape(2, 3, 1).tolist()
        self.assertEqual(list_flatten(lst), list(range(6)))


if __name__ == '__main__':
    unittest.main()
