#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-06 02:03:55
# @Author  : Kelley HUANG (dianhuangkan@gmail.com)
# @Link    : https://leetcode.com/problems/set-matrix-zeroes/
# @Ref     : https://cloud.tencent.com/developer/article/1775937

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # extra O(1) space
        m, n = len(matrix), len(matrix[0])
        first_row, first_col = False, False  # extra O(1) space

        # 特别的0的位置
        if matrix[0][0] == 0:
            first_row, first_col = True, True

        for _ in range(m):  # first col
            if matrix[_][0] == 0:
                first_col = True
                break
        for _ in range(n):  # first row
            if matrix[0][_] == 0:
                first_row = True
                break

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # found a zero
                    matrix[i][0] = 0  # 第i行的最上方作为标记
                    matrix[0][j] = 0  # 第j列的最左方作为标记

        for i in range(1, m):
            for j in range(1, n):
                # 如果最上方 or 最左方存在标记
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row:
            for _ in range(n):
                matrix[0][_] = 0
        if first_col:
            for _ in range(m):
                matrix[_][0] = 0

        return matrix

    def setZeroesByRowColNos(self, matrix):

        zero_row_nos, zero_col_nos = self.find_zero_rows_cols(matrix)
        # print(zero_row_nos, zero_col_nos)

        for i in zero_row_nos:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        for j in zero_col_nos:
            for i in range(len(matrix)):
                matrix[i][j] = 0

        return matrix

    def find_zeros(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[tuple(int, int)]
        """
        # extra O(mn) space
        zero_locs = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_locs.append((i, j))
        return zero_locs

    def find_zero_rows_cols(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[tuple(int, int)]
        """
        # 坐标去重
        # 直接找zero位置的横坐标、纵坐标
        # 而不是遍历整个矩阵查找所有的0
        # extra O(m+n) space
        zero_row_nos = []
        zero_col_nos = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i not in zero_row_nos:
                        zero_row_nos.append(i)
                    if j not in zero_col_nos:
                        zero_col_nos.append(j)

        return zero_row_nos, zero_col_nos


def main():
    matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]  # => [[1,0,1],[0,0,0],[1,0,1]]
    matrix = [[1, 0, 3]]  # => [[0,0,0]]
    sol = Solution()
    print(matrix, '\n')
    matrix = sol.setZeroes(matrix)
    print('\n', matrix)


if __name__ == '__main__':
    main()
