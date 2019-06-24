#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-24 21:11:06
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import itertools
from linkedlist import SLinkedList


class GraphNode(object):
    """
    图的节点，C风格写法
    """

    def __init__(self, data=None, adjacent: SLinkedList = None):
        self.data = data
        self.adjacent = adjacent
        self.adjacent_set = None  # TODO 使用Python的set数据结构


if __name__ == "__main__":
    island_grids = [["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"]]
    # 矩阵转化为图
    l = []
    h = len(test)
    w = len(test[0])
    coords = list(itertools.product(list(range(h)), list(range(w))))
    for c in coords:
        data = (c, test[c[0]][c[1]])  # 坐标元组 和 数据 # 这样数据存了两份，但好处是原来的矩阵不需要了
        # 双指针法构造邻接链表
        adj = None  # SLinkedList()
        ptr = None
        # 邻接表存的是索引，不是指针，索引可以用hash
        # 但这里用顺序表
        # 上下左右，相邻
        for c2 in [(c[0]+1, c[1]), (c[0]-1, c[1]), (c[0], c[1]+1), (c[0], c[1]-1)]:
            if (0 <= c2[0] < h) and (0 <= c2[1] < w):
                new = SLinkedList(data=c2, next=None)
                if not ptr:
                    ptr = new
                    adj = ptr
                else:
                    ptr.next = new
                    ptr = ptr.next

        node = GraphNode(data=data, adjacent=adj)
        l.append(node)  # l中存入元素

    print(l[0].adjacent)
    # traverse
    l[7].adjacent.traverse()
