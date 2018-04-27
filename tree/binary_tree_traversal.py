#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
      1
      /\
     /  \
    /    \
    2     3
   /\    /
  4  5  6
 /     /\
7     8  9

有四种方式：

前序遍历(PreorderTraversal, NLR): 先访问根结点，然后遍历其左右子树；结果：1 2 4 7 5 3 6 8 9
中序遍历(InorderTraversal, LNR): 先访问左子树，然后访问根节点，再访问右子树；结果：7 4 2 5 1 8 6 9 3
后序遍历(PostorderTraversal, LRN): 先访问左右子树，再访问根结点；结果：7 4 5 2 8 9 6 3 1
层序遍历(levelorderTraversal): 按照从上到下的层顺序访问；结果：1 2 3 4 5 6 7 8 9
'''
from __future__ import print_function
import unittest


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree(object):
    def __init__(self, newNode=None):
        self.root = newNode

def preorder(node, res=None):
    if res is None: res = []
    if node:
        res.append(node.val)
        preorder(node.left, res)
        preorder(node.right, res)
    return res or None

def inorder(node, res=None):
    if res is None: res = []
    if node:
        inorder(node.left, res)
        res.append(node.val)
        inorder(node.right, res)
    return res or None

def postorder(node, res=None):
    if res is None: res = []
    if node:
        postorder(node.left, res)
        postorder(node.right, res)
        res.append(node.val)
    return res or None


def levelorder(node, res=None):
    res = []
    if node:
        current_level = [node]
        while current_level:
            next_level = []
            for node in current_level:
                res.append(node.val)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            current_level = next_level
    return res or None


class TestBinaryTreeTravesal(unittest.TestCase):
    def setUp(self):
        self.tree = Node(1,
                         Node(2,
                              Node(4,
                                   Node(7, None, None),
                                   None),
                              Node(5, None, None)),
                         Node(3,
                              Node(6,
                                   Node(8, None, None),
                                   Node(9, None, None)),
                              None))

    def test_preorder(self):
        self.assertIsNone(preorder(None))
        self.assertEqual(preorder(self.tree), [1, 2, 4, 7, 5, 3, 6, 8, 9])

    def test_inorder(self):
        self.assertIsNone(inorder(None))
        self.assertEqual(inorder(self.tree), [7, 4, 2, 5, 1, 8, 6, 9, 3])

    def test_postorder(self):
        self.assertIsNone(postorder(None))
        self.assertEqual(postorder(self.tree), [7, 4, 5, 2, 8, 9, 6, 3, 1])

    def test_levelorder(self):
        self.assertIsNone(levelorder(None))
        self.assertEqual(levelorder(self.tree), [1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':

    unittest.main()
