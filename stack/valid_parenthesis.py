#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string containing just the characters
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
The brackets must close in the correct order,
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

import unittest
from stack import Stack

def is_valid_parenthesis(string):
    stack = Stack()
    dic = { ")":"(",
            "}":"{",
            "]":"["}
    for char in string:
        if char in dic.values():
            stack.push(char)
        elif char in dic.keys():
            if stack.isEmpty():
                return False
            s = stack.pop()
            if dic.get(char) != s:
                return False
    return stack.isEmpty()

if __name__ == '__main__':

    class TestValidPars(unittest.TestCase):
        def test_valid_pars(self):
            self.assertTrue(is_valid_parenthesis('(())'))
            self.assertTrue(is_valid_parenthesis('([])'))
            self.assertTrue(is_valid_parenthesis('{([])}'))

            self.assertFalse(is_valid_parenthesis('())'))
            self.assertFalse(is_valid_parenthesis('([(])'))
            self.assertFalse(is_valid_parenthesis('{[])}'))

    unittest.main()
