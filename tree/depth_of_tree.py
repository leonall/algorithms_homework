#!/usr/bin/env python
# -*- coding: utf-8 -*-


from binary_search_tree import BinarySearchTree

def get_depth(node):
    if node is None:
        return 0
    else:
        return 1 + max(get_depth(node.left), get_depth(node.right))


if __name__ == '__main__':

    tree = BinarySearchTree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    tree.add(-1)
    tree.add(16)
    tree.add(-5)
    tree.traverse()
    print('the depth of tree is: {}'.format(get_depth(tree.root)))

    '''
    3
    0  4
    -1  2  8
    -5  16
    the depth of tree is: 4
    '''
