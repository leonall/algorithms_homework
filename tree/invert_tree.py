#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Input:
     5
   /   \
  2     7
 / \   / \
1   3 6   9

Output:
     5
   /   \
  7     2
 / \   / \
9   6 3   1
'''

from binary_search_tree import BinarySearchTree


def reverse_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    if root.left:
        reverse_tree(root.left)
    if root.right:
        reverse_tree(root.right)


if __name__ == '__main__':

    tree = BinarySearchTree()
    map(tree.add, [5, 2, 7, 1, 3, 6, 9])
    tree.traverse()
    reverse_tree(tree.root)
    tree.traverse()

    '''
    5
    2  7
    1  3  6  9
    5
    7  2
    9  6  3  1
    '''
