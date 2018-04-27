#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Binary tree vs Binary search tree

https://stackoverflow.com/questions/6380231/difference-between-binary-tree-and-binary-search-tree

Binary tree: Tree where each node has up to two leaves
  1
 / \
2   3

Binary search tree: Used for searching.
A binary tree where the left child contains only nodes with values less than the parent node,
and where the right child only contains nodes with values greater than or equal to the parent.
  2
 / \
1   3

Python implement binary search tree comes from
https://stackoverflow.com/questions/2598437/how-to-implement-a-binary-tree
'''

from __future__ import print_function

class Node(object):
    def __init__(self, val):
        self.left = None
        self.right= None
        self.value = val

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.value):
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right= Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            raise ValueError('{} is not in tree'.format(val))

    def _find(self, val, node):
        if val == node.value:
            return node
        elif(val < node.value and node.left is not None):
            return self._find(val, node.left)
        elif(val > node.value and node.right is not None):
            return self._find(val, node.right)
        else:
            raise ValueError('{} is not in tree'.format(val))

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            print(str(node.value) + ' ')
            self._printTree(node.left)
            self._printTree(node.right)

    # def levelorder(self, node, more=None):
    #     if node is not None:
    #         if more is None:
    #             more = []
    #         more += [node.left, node.right]
    #         print(node.value)
    #     if more:
    #         self.levelorder(more[0], more[1:])

    def traverse(self):
        if self.root is not None:
            thislevel = [self.root]
            while thislevel:
                nextlevel = list()
                for n in thislevel:
                    print(n.value, end='  ')
                    if n.left: nextlevel.append(n.left)
                    if n.right: nextlevel.append(n.right)
                print()
                thislevel = nextlevel

if __name__ == '__main__':
    '''
         3
     0     4
       2      8
    '''
    tree = BinarySearchTree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    tree.add(-1)
    tree.add(3)
    tree.traverse()
    # tree.printTree()
    # print(tree.find(3).value)
    # print(tree.find(0).value)
    # tree.deleteTree()
    # tree.printTree()
