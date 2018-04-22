#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://nbviewer.jupyter.org/github/donnemartin/interactive-coding-challenges/
blob/master/linked_lists/remove_duplicates/remove_duplicates_solution.ipynb
"""

from single_linkedlist import SingleLinkedList
import numpy as np
import unittest


class NoDuplicatesLinkedList(SingleLinkedList):

    def __init__(self):
        super(NoDuplicatesLinkedList, self).__init__()

    def remove_dupes(self):
        if self.head is not None:
            node = self.head
            seen_node = set()
            while node is not None:
                if node.data not in seen_node:
                    seen_node.add(node.data)
                    prev = node
                    node = node.next
                else:
                    prev.next = node.next
                    node = node.next

    def remove_dupes2(self):
        if self.head is not None:
            node = self.head
            seen_node = set({node.data})
            while node.next is not None:
                if node.next.data in seen_node:
                    node.next = node.next.next
                else:
                    seen_node.add(node.next.data)
                    node = node.next


if __name__ == '__main__':

    class TestNoDuplicatesLinkedList(unittest.TestCase):

        def setUp(self):
            self.nums = 5

        def _setUp(self):
            self.linkedlist = NoDuplicatesLinkedList()
            self.set = set()
            vars = np.random.randint(0, 5, self.nums)
            for var in vars:
                self.linkedlist.add(var)
                self.set.add(var)

        def test_remove_dupes(self):
            for _ in range(10):
                self._setUp()
                self.assertEqual(len(self.linkedlist), self.nums)
                self.linkedlist.remove_dupes()
                self.assertEqual(len(self.linkedlist), len(self.set))

        def test_remove_dupes2(self):
            for _ in range(10):
                self._setUp()
                self.assertEqual(len(self.linkedlist), self.nums)
                self.linkedlist.remove_dupes2()
                self.assertEqual(len(self.linkedlist), len(self.set))

    unittest.main()
