#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024/08/16 00:58:01
# @Author  : Kelley HUANG (dianhuangkan@gmail.com)
# @Ref     : https://leetcode.com/problems/number-of-islands/

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        :type grid: List[List[str]
        :rtype: int
        """
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    res += 1
        return res

    def dfs(self, grid, i, j):
        dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        grid[i][j] = "0"
        for dir in dirs:
            nr, nc = i+dir[0], j+dir[1]
            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                if grid[nr][nc] == "1":
                    self.dfs(grid, nr, nc)


def main():
    test1 = [["1", "1", "1", "1", "0"],
             ["1", "1", "0", "1", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "0", "0", "0"]]
    sol = Solution()
    print(sol.numIslands(test1))


if __name__ == "__main__":
    main()
