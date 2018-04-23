#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are given two non-empty linked lists representing
two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero,
except the number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

https://github.com/yunshuipiao/algorithms/blob/master/linkedlist/add_two_numbers.py
"""

from single_linkedlist import SingleLinkedList
import numpy as np
import unittest

def add_two_numbers(left_linkedlist, right_linkedlist):
    """
    :param left_linkedlist: SingleLinkedList
    :param right_linkedlist: SingleLinkedList
    :return: SingleLinkedList
    """
    if not (isinstance(left_linkedlist, SingleLinkedList) and
            isinstance(right_linkedlist, SingleLinkedList)):
        raise ValueError('input arguments is not SingleLinkedList instance')
    else:
        left = left_linkedlist.head
        right = right_linkedlist.head
        pre_bit = 0
        res = SingleLinkedList()
        while left is not None and right is not None:
            v1 = left.data
            v2 = right.data
            cur_sum = v1 + v2 + pre_bit
            cur_bit = cur_sum % 10
            pre_bit = cur_sum // 10
            res.add(cur_bit)
            left = left.next
            right = right.next
        if pre_bit >= 1:
            res.add(pre_bit)
        return res


class TestNoDuplicatesLinkedList(unittest.TestCase):

    def _setUp(self):
        self.left, self.right = SingleLinkedList(), SingleLinkedList()

    def integer_to_list(self, integer):
        '''
        123 --> [3, 2, 1]
        '''
        return list(map(int, str(integer)))[::-1]

    def list_to_integer(self, lst):
        '''
        [1, 2, 3] --> 321
        '''
        integer = 0
        for bit, val in enumerate(lst):
            integer += val * 10 ** bit
        return integer

    def test_add_two_numbers(self):
        self._setUp()
        [self.left.add(i) for i in (2, 4, 3)]
        [self.right.add(i) for i in (5, 6, 4)]
        res = add_two_numbers(self.left, self.right)
        self.assertEqual(res.tolist(), [7, 0, 8])

    def test_add_two_numbers2(self):
        self._setUp()
        [self.left.add(i) for i in (2, 4, 6)]
        [self.right.add(i) for i in (5, 6, 4)]
        res = add_two_numbers(self.left, self.right)
        self.assertEqual(res.tolist(), [7, 0, 1, 1])

    def test_add_two_numbers3(self):
        for _ in range(10):
            self._setUp()
            left = np.random.randint(100, 999)
            right = np.random.randint(100, 999)
            _sum = left + right
            [self.left.add(i) for i in self.integer_to_list(left)]
            [self.right.add(i) for i in self.integer_to_list(right)]
            res = add_two_numbers(self.left, self.right)
            self.assertEqual(res.tolist(), self.integer_to_list(_sum))


if __name__ == '__main__':

    unittest.main()
