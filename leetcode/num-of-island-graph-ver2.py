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


def BFS(adj, start=None):
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
    n = len(adj[0])
    visited = [0 for i in range(n)]
    visited[start] = 1
    while queue:
        start = queue[0]
        for i in range(len(adj[start])):
            if adj[start][i] == 1 and visited[i] == 0:
                # visit(i)
                visited[i] = 1
                queue.append(i)
        del queue[0]
    return visited


class Solution:
    def numIslands(self, grid: list) -> int:
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
        print("1 coords", len(one_coords))
        input()
        n = len(one_coords)  # 27141个1
        start = time.clock()
        adj = [[0 for i in range(n)] for j in range(n)]  # 27141 * 27141
        elapsed = (time.clock() - start)  # 43.808438s
        print(elapsed)
        input()
        """
        不能用排列组合法构建，只要判断相邻的两个点就行
        有的点不是相邻的，不用组合在一起
        """
        combs = itertools.combinations(list(range(n)), 2)  # 27141 * 27140 / 2
        for comb in combs:
            i, j = comb
            ith_coord = one_coords[i]
            jth_coord = one_coords[j]
            if jth_coord in [(ith_coord[0]+1, ith_coord[1]), (ith_coord[0]-1, ith_coord[1]), (ith_coord[0], ith_coord[1]+1), (ith_coord[0], ith_coord[1]-1)]:
                adj[i][j], adj[j][i] = 1, 1

        # adj, one_coords, n
        visited = [0 for i in range(n)]
        # start = 0
        num_of_islands = 0
        while 0 in visited:
            start = visited.index(0)
            this_visited = BFS(adj, start)
            for i in range(n):
                visited[i] = visited[i] ^ this_visited[i]
            num_of_islands += 1

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

    grid = test46
    """
    test46
    219 * 250 = 54750个坐标
    27141 个1
    """
    s = Solution()
    num_of_islands = s.numIslands(grid)
    print(num_of_islands)


if __name__ == "__main__":
    main()
