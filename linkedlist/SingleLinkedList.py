#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://github.com/wangpanjun/datastructure/blob/master/linkedlist/singleLinkedList.md
'''

from __future__ import print_function


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList(object):
    def __init__(self):
        """初始化链表"""
        self.head = None

    """获取链表长度"""

    def __len__(self):
        current_node = self.head
        length = 0
        while current_node:
            length += 1
            current_node = current_node.next
        return length

    """判断链表是否为空"""

    def is_empty(self):
        return False if len(self) > 0 else True

    """追加节点"""

    def add(self, data):
        """
        1.head 是 None: head --> node
        2.head 不是 None: tail.next --> node
        :param data:
        :return:
        """
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node

    """插入节点"""

    def insert(self, index, data):
        """
        1.index 插入节点位置包括正负数
        2.找到index-1-->current_node的节点
        3.current_node.next-->node
          node.next-->current_node.next.next
        4.head
        :param index:
        :param data:
        :return:
        """
        node = Node(data)
        if abs(index + 1) > len(self):
            return False
        index = index if index >= 0 else len(self) + index + 1
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            current_node = self.get(index - 1)
            if current_node:
                current_node_next = current_node.next
                current_node.next = node
                node.next = current_node_next
            else:
                return False
        return node

    """反转链表"""

    def __reversed__(self):
        """
        1.current-->next 转变为 next-->current
        2.current 若是head 则把 current.next --> None
        3.tail-->self.head
        :return:
        """
        def reverse(current_node, node):
            if current_node is self.head:
                current_node.next = None
            if node:
                next_node = node.next
                node.next = current_node
                return reverse(node, next_node)
            else:
                self.head = current_node
        return reverse(self.head, self.head.next)

    # def __reversed__(self):
    #     """
    #     1.current-->next 转变为 next-->current
    #     2.current 若是head 则把 current.next --> None
    #     3.tail-->self.head
    #     :return:
    #     """
    #     if self.head:
    #         current_node = self.head
    #         next_node = current_node.next
    #         current_node.next = None
    #         while next_node:
    #             prev_node = current_node
    #             current_node = next_node
    #             next_node = next_node.next
    #             current_node.next = prev_node
    #     self.head = current_node


    """获取节点"""

    def get(self, index):
        """
        :param index:
        :return:
        """
        index = index if index >= 0 else len(self) + index
        if len(self) < index or index < 0:
            return None
        current = self.head
        while index:
            current = current.next
            index -= 1
        return current

    """查找节点"""

    def search(self, target):
        """
        :param data:
        :return: index
        """
        index = 0
        current = self.head
        Found = False
        while current and not Found:
            if current.data == target:
                Found = True
                break
            else:
                index += 1
                current = current.next
        return Found and index

    """设置节点"""

    def set(self, index, data):
        node = self.get(index)
        if node:
            node.data = data
        return node

    """删除某个元素"""

    def remove(self, index):
        f = index if index > 0 else abs(index + 1)
        if len(self) <= f:
            return False
        current = self.head
        index = index if index >= 0 else len(self) + index
        currentp = None
        while index:
            currentp = current
            current = current.next
            index -= 1
        if not currentp:
            self.head = current.next
        else:
            currentp.next = current.next
        return current.data

    """清空链表"""

    def clear(self):
        self.head = None

    """打印链表"""

    def show(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


if __name__ == '__main__':
    ls = SingleLinkedList()
    print('New created linkedlist is empty? {}'.format(ls.is_empty()))
    ls.add(1)
    print('After add 1, Linkedlist is empty now? {}'.format(ls.is_empty()))
    ls.add(2)
    ls.add(3)
    format = "{}-->index: {} ".format
    print(list(map(format, [1, 2, 3], [ls.search(1), ls.search(2), ls.search(3)])))

    ls.insert(-1, 10)
    ls.show()
    print(ls.get(-1).data)
    reversed(ls)
    ls.show()
    print(ls.get(0).data)
    ls.show()
    ls.remove(2)
    ls.show()
    ls.set(-12, 20)
    ls.show()
