#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-24 20:24:23
# @Author  : Your Name (you@example.org)
# @Link    : https://leetcode.com/problems/number-of-islands
# @Version : $Id$

import os
import itertools


def belongTo(c: tuple, island: list):
    for _ in island:
        if c in [(_[0]+1, _[1]), (_[0]-1, _[1]), (_[0], _[1]+1), (_[0], _[1]-1)]:
            return True
    return False


def merge(islands: list) -> list:
    """
    等待归并的几个集合
    """
    merged = []
    island = islands.pop(0)
    while islands:
        i = 0
        for _ in islands.copy():
            for c in _:
                if belongTo(c, _):
                    island += islands.pop(i)
            i += 1
        merged.append(island)
    return merged


class Solution:
    def numIslands(self, grid: list) -> int:
        if grid == []:
            return 0
        h = len(grid)
        w = len(grid[0])
        coords = list(itertools.product(list(range(h)), list(range(w))))
        # print(coords)
        one_coords = []
        for c in coords:
            if grid[c[0]][c[1]] == '1':
                one_coords.append(c)
        # print(one_coords)
        if one_coords == []:
            return 0
        islands = []
        island = []

        for c in one_coords:
            if island == []:
                island.append(c)
                continue
            if belongTo(c, island):
                island.append(c)
            else:  # 新集合
                islands.append(island)
                island = [c]
        # 最后一个
        islands.append(island)
        islands = merge(islands)
        print(islands)
        return len(islands)


def main():
    test = [["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]]
    test2 = [["1", "1", "0", "0", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"]]
    test3 = [["1", "1", "1"],
             ["0", "1", "0"],
             ["1", "1", "1"]]
    sol = Solution()
    # belongTo((3, 3), test2)
    print(sol.numIslands(test3))


if __name__ == "__main__":
    main()
