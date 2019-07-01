#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-24 21:11:06
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import itertools
from test46 import test46
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
    visited = [0 for i in range(n)]
    visited[start] = 1
    while queue:
        start = queue[0]
        for i in range(n):
            _ = start
            _i = i
            if _ > _i:
                _, _i = _i, _
            if (_, _i) in adj and visited[i] == 0:
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

        h = len(grid)
        w = len(grid[0])

        coords = list(itertools.product(list(range(h)), list(range(w))))
        one_coords = []
        for c in coords:
            if grid[c[0]][c[1]] == '1':
                one_coords.append(c)

        print("1 coords num:", len(one_coords))
        print(one_coords)
        n = len(one_coords)  # 27141个1

        """
        # 27141 * 27141
        # 43.808438s
        adj = [[0 for i in range(n)] for j in range(n)]
        """
        """
        start = time.clock()
        adj0 = [0] * n
        # 13.910593s
        # Space: O(n^2) = 27141 * 27141
        adj = [adj0.copy() for i in range(n)]
        elapsed = (time.clock() - start)
        print(elapsed)
        input("0初始化完成，继续？")
        """
        """
        不能用排列组合法构建，只要判断相邻的两个点就行
        有的点不是相邻的，不用组合在一起
        """

        """
        # 两两组合，组合数太多，只考虑相邻的即可
        combs = itertools.combinations(list(range(n)), 2)  # 27141 * 27140 / 2
        for comb in combs:
            i, j = comb
            ith_coord = one_coords[i]
            jth_coord = one_coords[j]
            if jth_coord in [(ith_coord[0]+1, ith_coord[1]), (ith_coord[0]-1, ith_coord[1]), (ith_coord[0], ith_coord[1]+1), (ith_coord[0], ith_coord[1]-1)]:
                adj[i][j], adj[j][i] = 1, 1
        """
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
        '''
        print(elapsed)
        input("adj初始化完成，继续？")
        print(adj)
        input("adj初始化完成，继续？")
        '''
        visited = [0 for i in range(n)]
        num_of_islands = 0
        while 0 in visited:
            start = visited.index(0)
            this_visited = BFS(adj, n, start)
            for i in range(n):
                visited[i] = visited[i] | this_visited[i]
            num_of_islands += 1
            print(sum(visited))
        return num_of_islands


def main():
    test1 = [["1", "1", "1", "1", "0"],
             ["1", "1", "0", "1", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "0", "0", "0"]]
    test2 = [["1", "1", "0", "0", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"]]
    test33 = [["1", "1", "1"],
              ["0", "1", "0"],
              ["1", "1", "1"]]
    grid = test46
    """
    test46
    219 * 250 = 54750个坐标
    27141 个1
    109 个岛，要算好久好久
    """
    s = Solution()
    num_of_islands = s.numIslands(grid)
    print(num_of_islands)


if __name__ == "__main__":
    main()
