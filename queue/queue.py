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


class Quque(object):

    def __init__(self, capacity=10):
        """
        Initialize python List with capacity of 10 or user given input.
        Python List type is a dynamic array, so we have to restrict its
        dynamic nature to make it work like a static array.
        """
        self._array = [None] * capacity
        self._front = 0
        self._rear = 0

    def _size(self):
        return self._rear - self._front

    def __len__(self):
        return self._size()

    def enqueue(self, item):
        if self._rear == len(self._array):
            self._expend()
        self._array[self._rear] = item
        self._rear += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue is empty!')
        value = self._array[self._front]
        self._array[self._front] = None
        self._front += 1
        return value

    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue is empty!')
        else:
            return self._array[self._front]

    def isEmpty(self):
        return self._rear == self._front

    def _expend(self):
        '''
        double the size of the queue
        '''
        NewArray = [None] * len(self._array) * 2
        for i, item in enumerate(self._array):
            NewArray[i] = self._array[i]
        self._array = NewArray

    def __iter__(self):
        if self.isEmpty():
            raise IndexError('Queue is empty!')
        i = self._front
        while True:
            if i < self._rear:
                yield self._array[i]
                i += 1
            else:
                raise StopIteration


class TestQuque(unittest.TestCase):

    def _setUp(self):
        self.queue = Quque()
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
