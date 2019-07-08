#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-08-19 15:53
# @Author  : Your Name (you@example.org)
# @Link    : https://leetcode.com/problems/subsets/

"""
If S = [1,2,3], a solution is: [ [3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], []
"""
import pysnooper
import os

'''
取e0，剩下的遍历
取
'''
'''
递归
子集就是自己，加拆掉一个元素，（被拆掉的不用管），len n-1的子列表的子集
子集的子集
'''
res = []
res.append([])
print(res)


def subset(S: list, res: list):
    # 终止条件
    if S not in res:
        res.append(S)
    if len(S) == 1:
        return
    for e in S:
        _ = S.copy()
        _.remove(e)
        subset(_, res)


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
    print(res)


if __name__ == "__main__":
    main()
