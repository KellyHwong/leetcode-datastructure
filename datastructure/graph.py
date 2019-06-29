#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-24 20:20:50
# @Author  : Your Name (you@example.org)
# @Link    : https://zh.wikipedia.org/wiki/%E5%9B%BE_(%E6%95%B0%E5%AD%A6)
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


mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12]]

"""
i, j = 0 意思是i节点指向j节点
"""
adj = [[0, 1, 1, 0, 0],
       [0, 0, 1, 1, 0],
       [0, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [0, 0, 1, 1, 0]]


def visit(i):
    print("Node %d visited!" % i)


def BFS(adj):
    """
    广度优先
    先看周围（邻接的点）
    再看周围的周围
    有点类似二叉树层序初始化
    控制访问的方法是设置flag
    """

    start = 0  # 从第一个节点开始
    queue = [start]
    visit(start)
    visited = [1, 0, 0, 0, 0]
    while queue:
        start = queue[0]
        for i in range(len(adj[start])):
            if adj[start][i] == 1 and visited[i] == 0:
                visit(i)
                visited[i] = 1
                queue.append(i)
        del queue[0]


def DFS(adj):
    """
    深度优先
    TODO
    """

    start = 0  # 从第一个节点开始
    queue = [start]
    visit(start)
    visited = [1, 0, 0, 0, 0]
    while queue:
        start = queue[0]
        for i in range(len(adj[start])):
            if adj[start][i] == 1 and visited[i] == 0:
                visit(i)
                visited[i] = 1
                queue.append(i)
        del queue[0]


if __name__ == "__main__":
    BFS(adj)
