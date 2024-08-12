#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jun-14-21 17:04
# @Author  : Kan HUANG (dianhuangkan@gmail.com)

from typing import Any


class ListNode(object):
    """单链表的节点，ListNode or LinkedList/SLinkedList
    Python风格，对象本身就是对象的指针。
    命名的时候用Node表示当作节点，用List表示节点的指针和一段链表。
    """

    def __init__(self, data: Any = None, next=None):
        self.data = data
        self.next = next

    def traverse(self):
        """以yield的形式返回整段链表的节点元素的数据。
        """
        ptr = self
        while ptr:
            # print(ptr.data)
            yield ptr.data
            ptr = ptr.next

    def reverse(self):
        """三指针法翻转单链表
        """
        p, q = self, self.next
        self.next = None
        while q:
            r = q.next
            q.next = p
            p = q
            q = r
        self = p

    def recursiveReverse(self):
        pass


def main():
    # Nodes
    n1 = ListNode("Mon")
    n2 = ListNode("Tue")
    n3 = ListNode("Wed")
    n4 = ListNode("Thur")
    n5 = ListNode("Fri")
    n6 = ListNode("Sat")
    n7 = ListNode("Sun")

    # Linking
    n6.next = n7
    n5.next = n6
    n4.next = n5
    n3.next = n4
    n2.next = n3
    n1.next = n2

    # List
    linked_list = n1

    '''
    print(e2.next)
    # 结果为e3内存地址<__main__.Node object at 0x0000001A0F9644BE0>
    print(e2.next.data)
    # 结果为e3所代表的值Wed
    '''

    for d in iter(n1.traverse()):
        print(d)

    linked_list.reverse()
    # for
    for d in iter(n7.traverse()):
        print(d)


if __name__ == "__main__":
    main()
