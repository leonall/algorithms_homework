#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import unittest

class StackNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListStack(object):
    def __init__(self):
        self.top = 0
        self.head = None

    def isEmpty(self):
        return self.top == 0

    def __len__(self):
        return self.top

    def push(self, value):
        node = StackNode(value)
        node.next = self.head
        self.head = node
        self.top += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        value = self.head.value
        self.head = self.head.next
        self.top -= 1
        return value

    def peek(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        return self.head.value

    def __iter__(self):
        probe = self.head
        while True:
            if probe is None:
                raise StopIteration
            yield probe.value
            probe = probe.next


class TestLinkedListStack(unittest.TestCase):

    def _setUp(self):
        self.stack = LinkedListStack()
        self._lst = []
        for i in np.random.randint(0, 10, 10):
            self.stack.push(i)
            self._lst.append(i)
        self._lst = self._lst[::-1]

    def test_LinkedListStack(self):
        for _ in range(10):
            self._setUp()
            self.assertEqual(len(self.stack), len(self._lst))
            self.assertEqual(self.stack.peek(), self._lst[0])
            self.assertEqual(self.stack.pop(), self._lst[0])
            self.assertFalse(self.stack.isEmpty())
            for i, val in enumerate(self.stack):
                self.assertEqual(val, self._lst[i+1])
                self.assertEqual(self.stack.pop(), self._lst[i+1])
            self.assertTrue(self.stack.isEmpty())


if __name__ == '__main__':
    unittest.main()
