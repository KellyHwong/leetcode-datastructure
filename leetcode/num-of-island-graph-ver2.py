#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-24 21:11:06
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import itertools
import time


def BFS(adj: dict, n, start=None):
    """
    广度优先
    先看周围（邻接的点）
    再看周围的周围
    有点类似二叉树层序初始化
    控制访问的方法是设置flag
    """

    if not start:
        start = 0  # 从第一个节点开始
    queue = [start]
    # visit(start)
    # n = len(adj[0])
    visited = [0 for i in range(n)]
    visited[start] = 1
    while queue:
        start = queue[0]
        for i in range(n):
            _ = start
            if _ > i:
                _, i = i, _
            if (_, i) in adj and visited[i] == 0:
                # visit(i)
                visited[i] = 1
                queue.append(i)
        del queue[0]
    return visited


class Solution:
    def numIslands(self, grid: list) -> int:
        """
        方法一：把所有1的邻接矩阵构造出来，然后BFS
        方法二：边遍历边构造，0的时候停止
        """
        if grid == []:
            return 0
        # 矩阵转化为图
        h = len(grid)
        w = len(grid[0])

        coords = list(itertools.product(list(range(h)), list(range(w))))
        one_coords = []
        for c in coords:
            if grid[c[0]][c[1]] == '1':
                one_coords.append(c)
        n = len(one_coords)  # 27141个1
        adj = dict()
        start = time.clock()
        # 按照1的坐标
        for i in range(n):
            ith_coord = one_coords[i]
            # 上下左右
            for jth_coord in [(ith_coord[0]+1, ith_coord[1]),
                              (ith_coord[0]-1, ith_coord[1]),
                              (ith_coord[0], ith_coord[1]+1),
                              (ith_coord[0], ith_coord[1]-1)]:
                # 范围
                if 0 <= jth_coord[0] < h and 0 <= jth_coord[1] < w:
                    if grid[jth_coord[0]][jth_coord[1]] == '1':
                        j = one_coords.index(jth_coord)
                        # adj[(i, j)], adj[(j, i)] = 1, 1 # 只存一半
                        _i = i
                        _j = j
                        if _i > _j:
                            _i, _j = _j, _i
                        if (_i, _j) not in adj.keys():
                            adj[(_i, _j)] = '1'

        elapsed = (time.clock() - start)
        # adj, one_coords, n
        visited = [0 for i in range(n)]
        # start = 0
        num_of_islands = 0
        while 0 in visited:
            start = visited.index(0)
            this_visited = BFS(adj, n, start)
            for i in range(n):
                visited[i] = visited[i] | this_visited[i]
            num_of_islands += 1

        return num_of_islands
