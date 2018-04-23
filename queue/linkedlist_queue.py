#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Queue Abstract Data Type (ADT)
* Queue() creates a new queue that is empty.
  It needs no parameters and returns an empty queue.
* enqueue(item) adds a new item to the rear of the queue.
  It needs the item and returns nothing.
* dequeue() removes the front item from the queue.
  It needs no parameters and returns the item. The queue is modified.
* isEmpty() tests to see whether the queue is empty.
  It needs no parameters and returns a boolean value.
* size() returns the number of items in the queue.
  It needs no parameters and returns an integer.
* peek() returns the front element of the queue.
"""

import numpy as np
import unittest


class QueueNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListQuque(object):

    def __init__(self, capacity=10):
        self.head = None

    def _size(self):
        node = self.head
        i = 0
        while node is not None:
            i += 1
            node = node.next
        return i

    def __len__(self):
        return self._size()

    def enqueue(self, item):
        new_node = QueueNode(item)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue is empty!')
        value = self.head.value
        self.head = self.head.next
        return value

    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue is empty!')
        value = self.head.value
        return value

    def isEmpty(self):
        return self.head is None

    def __iter__(self):
        if self.isEmpty():
            raise IndexError('Queue is empty!')
        node = self.head
        while True:
            if node is not None:
                yield node.value
                node = node.next
            else:
                raise StopIteration


class TestQuque(unittest.TestCase):

    def _setUp(self):
        self.queue = LinkedListQuque()
        self._lst = []
        for i in np.random.randint(0, 10, 12):
            self.queue.enqueue(i)
            self._lst.append(i)

    def test_LinkedListStack(self):
        for _ in range(10):
            self._setUp()
            self.assertEqual(len(self.queue), len(self._lst))
            self.assertEqual(self.queue.peek(), self._lst[0])
            self.assertEqual(self.queue.dequeue(), self._lst[0])
            self.assertFalse(self.queue.isEmpty())
            for i, val in enumerate(self.queue):
                self.assertEqual(val, self._lst[i+1])
                self.assertEqual(self.queue.dequeue(), self._lst[i+1])
            self.assertTrue(self.queue.isEmpty())


if __name__ == '__main__':

    unittest.main()
