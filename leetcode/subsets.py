#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-08-19 21:07
# @Author  : Your Name (you@example.org)
# @Link    : https://leetcode.com/problems/subsets/

import os
import pysnooper

"""
一次遍历
"""


def subset(S, res):
    if len(S) == 1:
        return
    for i in range(len(S)-1):
        res.append([S[i]])
        left = S[:i]+S[i+1:]  # 切片产生复制
        res.append(left)
        subset(left, res)


class Solution:
    def subsets(self, nums: list) -> list:
        res = []
        subset(nums, res)
        res.append([])
        return res


@pysnooper.snoop()
def main():
    sol = Solution()
    nums = [1, 2, 3]
    nums = [3, 2, 4, 1]
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 10, 0]
    res = sol.subsets(nums)
    # print(res)


if __name__ == "__main__":
    main()
