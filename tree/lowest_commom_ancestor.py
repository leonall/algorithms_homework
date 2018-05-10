#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
          _10_
        /      \
       5        9
      / \      / \
     12  3    18  20
        / \       /
       1   8     40
0, 5 -> None
5, 0 -> None
1, 8 -> 3
12, 8 -> 5
12, 40 -> 10
9, 20 -> 9
3, 5 -> 5

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

    def _node_in_tree(self, root, node):
        if root is None:
            return False
        if node is root:
            return True
        left_flag = self._node_in_tree(root.left, node)
        right_flag = self._node_in_tree(root.right, node)
        return left_flag or right_flag

    def _lca(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root is p or root is q:
            return root
        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)
        if left and right:
            return root
        return left if left else right

    def lca(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not self._node_in_tree(self.root, p) or not self._node_in_tree(self.root, q):
            return None
        else:
            return self._lca(root, p, q)

class TestBinaryTreeTravesal(unittest.TestCase):
    def setUp(self):
        self.node10 = Node(10)
        self.node5 = Node(5)
        self.node12 = Node(12)
        self.node3 = Node(3)
        self.node1 = Node(1)
        self.node8 = Node(8)
        self.node9 = Node(9)
        self.node18 = Node(18)
        self.node20 = Node(20)
        self.node40 = Node(40)
        self.node3.left = self.node1
        self.node3.right = self.node8
        self.node5.left = self.node12
        self.node5.right = self.node3
        self.node20.left = self.node40
        self.node9.left = self.node18
        self.node9.right = self.node20
        self.node10.left = self.node5
        self.node10.right = self.node9
        self.node0 = Node(0)  # not in the tree, to test
        self.root = self.node10
        self.tree = Tree(newNode=self.root)

    def test_lca(self):
        self.assertEquals(self.tree.lca(self.root, self.node5, self.node9), self.node10)
        self.assertIsNone(self.tree.lca(self.root, self.node0, self.node5), None)
        self.assertIsNone(self.tree.lca(self.root, self.node5, self.node0), None)
        self.assertEquals(self.tree.lca(self.root, self.node1, self.node8), self.node3)
        self.assertEquals(self.tree.lca(self.root, self.node12, self.node8), self.node5)
        self.assertEquals(self.tree.lca(self.root, self.node12, self.node40), self.node10)
        self.assertEquals(self.tree.lca(self.root, self.node9, self.node20), self.node9)
        self.assertEquals(self.tree.lca(self.root, self.node3, self.node5), self.node5)

if __name__ == '__main__':

    unittest.main()
