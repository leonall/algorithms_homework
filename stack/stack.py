#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Stack Abstract Data Type (ADT)
Stack() creates a new stack that is empty.
   It needs no parameters and returns an empty stack.
push(item) adds a new item to the top of the stack.
   It needs the item and returns nothing.
pop() removes the top item from the stack.
   It needs no parameters and returns the item. The stack is modified.
peek() returns the top item from the stack but does not remove it.
   It needs no parameters. The stack is not modified.
isEmpty() tests to see whether the stack is empty.
   It needs no parameters and returns a boolean value.
size() returns the number of items on the stack.
   It needs no parameters and returns an integer.
'''

import numpy as np
import unittest


class Stack(object):

    def __init__(self, size=10):
        """
        Initialize python List with size of 10 or user given input.
        Python List type is a dynamic array, so we have to restrict its
        dynamic nature to make it work like a static array.
        """
        self._array = [None] * size
        self._top = 0

    def size(self):
        return self._top

    def __len__(self):
        return self._top

    def push(self, item):
        if self._top == len(self._array):
            self._expend()
        self._array[self._top] = item
        self._top += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError('Stack is empty!')
        value = self._array[self._top - 1]
        self._array[self._top - 1] = None
        self._top -= 1
        return value

    def peek(self):
        if self.isEmpty():
            raise IndexError('Stack is empty!')
        else:
            return self._array[self._top - 1]

    def isEmpty(self):
        return self._top == 0

    def _expend(self):
        '''
        double the size of the stack
        '''
        NewArray = [None] * len(self._array) * 2
        for i, item in enumerate(self._array):
            NewArray[i] = self._array[i]
        self._array = NewArray

    def __iter__(self):
        if self.isEmpty():
            raise IndexError('Stack is empty!')
        i = self._top
        while True:
            if i > 0:
                yield self._array[i-1]
                i -= 1
            else:
                raise StopIteration


class TestStack(unittest.TestCase):

    def _setUp(self):
        self.stack = Stack()
        self._lst = []
        for i in np.random.randint(0, 10, 21):
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
