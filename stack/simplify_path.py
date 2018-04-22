#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an absolute path for a file (Unix-style), simplify it.
For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
* Did you consider the case where path = "/../"?
    In this case, you should return "/".
* Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
    In this case, you should ignore redundant slashes and return "/home/foo".
"""

import unittest
from stack import Stack


def simplify_path(path):
    """
    :type path: str
    :rtype: str
    """
    skip = set(['..', '.', ''])
    stack = Stack()
    paths = path.split('/')
    for token in paths:
        if token == '..':
            if not stack.isEmpty():
                stack.pop()
        elif token not in skip:
            stack.push(token)
    return '/' + '/'.join(list(stack)[::-1])


if __name__ == '__main__':

    class TestSimplifyPath(unittest.TestCase):

        def setUp(self):
            self.p = '/my/name/is/..//keon'
            self.sp = '/my/name/keon'

        def test_simplify_path(self):
                self.assertEqual(simplify_path(self.p), self.sp)

    unittest.main()
