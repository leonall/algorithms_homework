#!/usr/bin/env python
# -*- coding: utf-8 -*-


from binary_search_tree import BinarySearchTree

def is_balance_tree(root):
    '''
    O(N) solution
    '''
    return -1 != get_depth(root)

def get_depth(root):
    """
    return 0 if unbalanced else depth + 1
    """
    if not root:
        return 0
    left = get_depth(root.left)
    right = get_depth(root.right)
    if left != right:
        return -1
    return 1 + max(left, right)


if __name__ == '__main__':

    tree = BinarySearchTree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    tree.add(-1)
    tree.add(16)
    tree.traverse()
    print('the tree is balance ? {}'.format(is_balance_tree(tree.root)))

    '''
    3
    0  4
    -1  2  8
    16
    the tree is balance ? False
    '''
