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
        self.array = [None] * 10
        self.top = 0

    def size(self):
        return self.top

    def __len__(self):
        return self.top

    def push(self, item):
        if self.top == len(self.array):
            self.expend()
        self.array[self.top] = item
        self.top += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError('Stack is empty!')
        value = self.array[self.top - 1]
        self.array[self.top - 1] = None
        self.top -= 1
        return value

    def peek(self):
        if self.isEmpty():
            raise IndexError('Stack is empty!')
        else:
            return self.array[self.top - 1]

    def isEmpty(self):
        return self.top == 0

    def expend(self):
        '''
        double the size of the stack
        '''
        NewArray = [None] * len(self.array) * 2
        for i, item in self.array:
            NewArray[i] = self.array[i]
        self.array = NewArray

    def __iter__(self):
        if self.isEmpty():
            raise IndexError('Stack is empty!')
        i = self.top
        while True:
            if i > 0:
                yield self.array[i-1]
                i -= 1
            else:
                raise StopIteration


class TestStack(unittest.TestCase):

    def _setUp(self):
        self.stack = Stack()
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
