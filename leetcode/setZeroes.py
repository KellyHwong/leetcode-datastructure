#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-06 02:03:55
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os


class Solution:
    def setZeroes(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix = 0

# 又是一个去重问题


class TestCase(object):
    """docstring for TestCase"""

    def __init__(self, input, output):
        self.input = input
        self.output = output


def main():
    matrix = [[1, 2, 0], [4, 5, 6]]
    zero_loc = (0, 2)
    for j in range(len(matrix[0])):
        matrix[zero_loc[0]][j] = 0
    for i in range(len(matrix)):
        matrix[i][zero_loc[1]] = 0
    print(matrix)


if __name__ == '__main__':
    main()
