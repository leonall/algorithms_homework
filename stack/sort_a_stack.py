#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1. sort stack by a array
2. sort stack by a stack

要求：

一个栈的元素为整型，现在想将该栈的从栈顶到底按从小到大的顺序排序，只许申请一个栈。

思考：

将要排序的栈记为 stack，申请辅助的栈记为 _stack，在 stack 栈执行 pop 操作，弹出的元素记为 top，
如果 top 大于 _stack 的栈顶元素，则将 top 压入 _stack；如果 top 小于 _stack 的栈顶元素，
则弹出 _stack 栈顶元素压入 stack 直到 top 的值大于等于 _stack 的栈顶元素。
依次运行，直到 stack 为空之后，把 _stack 的栈元素依次压入 stack 栈里即可。
"""

import unittest
import numpy as np
from stack import Stack

def sort(stack):
    """
    sort stack by a array
    :type stack: stack
    :rtype: stack
    """
    if len(stack) <= 1:
        return stack
    else:
        _stack = Stack()
        arr = []
        for val in stack:
            arr.append(val)
        arr = sorted(arr, reverse=True)
        for val in arr:
            _stack.push(val)
        return _stack


def sort2(stack):
    """
    sort stack by a stack
    :type stack: stack
    :rtype: stack
    """
    H = len(stack)
    if H <= 1:
        return stack
    else:
        _stack = Stack()
        while not stack.isEmpty():
            top = stack.pop()
            while not _stack.isEmpty() and top < _stack.peek():
                stack.push(_stack.pop())
            _stack.push(top)
        while not _stack.isEmpty():
            stack.push(_stack.pop())

        return stack


class TestSortStack(unittest.TestCase):

    def _setUp(self, seed):
        np.random.seed(seed)
        self.stack = Stack()
        self._lst = []
        for i in np.random.randint(0, 5, 10):
            self.stack.push(i)
            self._lst.append(i)
        self._lst = self._lst[::-1]

    def test_sort(self):
        for i in range(1):
            self._setUp(seed=10)
            self.assertEqual([v for v in sort(self.stack)], sorted(self._lst))

    def test_sort2(self):
        for i in range(1):
            self._setUp(seed=10)
            self.assertEqual([v for v in sort2(self.stack)], sorted(self._lst))

if __name__ == '__main__':

    unittest.main()
