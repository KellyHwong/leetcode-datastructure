#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-23 22:00:20
# @Author  : Your Name (you@example.org)
# @Link    : https://leetcode.com/problems/game-of-life/
# @Version : $Id$

import os
import itertools

def get_neighbors(coord, width, height):
    x, y = coord[0], coord[1]
    axis_x = [x - 1, x, x + 1]
    axis_y = [y - 1, y, y + 1]
    neighbors = [e for e in itertools.product(axis_x, axis_y)]
    neighbors.remove(coord)
    for neighbor in neighbors.copy():
        if (not neighbor[0] in range(height)) or (not neighbor[1] in range(width)):
            neighbors.remove(neighbor)
    return neighbors

def update(board, coord, width, height):
    neighbors = get_neighbors(coord, width, height)
    # print(neighbors)
    count = sum([1 for (x, y) in neighbors if board[x][y] == 1])
    # print(count)
    # return count
    (x, y) = coord
    if board[x][y] == 1:
        if count < 2:
            # return 0 die change
            return True
        elif 2 <= count <= 3:
            # 1 alive no change
            return False
        elif count > 3:
            # 0 die change
            return True
    elif board[x][y] == 0:
        if count == 3:
            # change to alive
            return True
    # by default
    return False

class Solution:
    def gameOfLife(self, board) -> None:  # board: List[List[int]]
        """
        Do not return anything, modify board in-place instead.
        :param list[list] board: storage of cells
        """
        width = len(board[0])
        height = len(board)

        axis_x = [e for e in range(width)]
        axis_y = [e for e in range(height)]
        coords = [e for e in itertools.product(axis_y, axis_x)]

        # coord = (1, 0)
        # print( update(board, coord, width, height) )
        to_update = []
        for coord in coords:
            (x, y) = coord
            if update(board, coord, width, height):
                to_update.append((x, y))
        for to_up in to_update:
            (x, y) = to_up
            board[x][y] = 1 - board[x][y]



def main():
    sol = Solution()
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    width = len(board[0])
    height = len(board)

    sol.gameOfLife(board)

    axis_x = [e for e in range(width)]
    axis_y = [e for e in range(height)]
    coords = [e for e in itertools.product(axis_y, axis_x)]

    # coord = (1, 0)
    # print( update(board, coord, width, height) )
    to_update = []
    for coord in coords:
        (x, y) = coord
        if update(board, coord, width, height):
            to_update.append((x, y))
    for to_up in to_update:
        (x, y) = to_up
        board[x][y] = 1 - board[x][y]
    print(board)

if __name__ == '__main__':
    main()
