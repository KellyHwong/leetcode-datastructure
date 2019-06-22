#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-16 00:41:05
# @Author  : Your Name (you@example.org)
# @Link    : https://zh.wikipedia.org/zh-cn/队列
# @Version : $Id$

import os


class Node():
    """docstring for QNode"""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkQueue():
    """docstring for LinkQueue"""
    """
    头指针front不需要data域，它的作用是指向链表
    尾指针rear初始化为与front相同
    注意他们都指向同一个Node对象
    但是这个对象的data域无效
    这个在初始化的时候设置的Node充当指针的作用
    这样可以通过比较front和rear的地址来判断is_empty
    而不需要设置一个length
    """

    def __init__(self, next=None):
        self.front = Node()
        self.rear = self.front
        # self.length = 0

    def destroy(self):
        pass

    def clear(self):
        pass

    def is_empty(self) -> bool:
        if self.front is self.rear:
            return True
        else:
            return False

    def function(self):
        pass

    def length(self):
        i = 0
        p = self.front
        # 遍历队列中的节点，直到队尾等于队头
        while self.rear != p:
            i += 1
            p = p.next
        return i

    def traverse(self):
        i = 0
        p = self.front
        while self.rear != p:
            i += 1
            print(p.next.data)
            p = p.next

    def traverseData(self):
        ret = []
        i = 0
        p = self.front
        print("traverseData")
        while self.rear != p:
            print(i)
            i += 1
            ret.append(p.next.data)
            p = p.next
        return ret

    def get_head(self):
        pass

    def push(self, data):
        # 入队
        p = Node()
        p.data = data
        p.next = None
        if self.is_empty():
            self.front.next = p # 如果是第一个元素
        # FIFO
        self.rear.next = p
        self.rear = p
    
    def pop(self):
        if self.front == self.rear:
            return False
        p = self.front.next
        e = p.data
        self.front.next = p.next
        if self.rear == p: # 如果是最后一个元素
            self.rear = self.front
        return e

def main():
    '''
    n1 = QNode()
    n2 = n1
    print(n1 == n2)
    print(n1 is n2)
    '''
    link_queue = LinkQueue()
    for i in range(10):
        link_queue.push(i)
    link_queue.traverse()
    print(link_queue.length())
    for j in range(10):
        print(link_queue.pop())
        print(link_queue.is_empty())

if __name__ == '__main__':
    main()
