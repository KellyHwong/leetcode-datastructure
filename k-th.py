#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-21 15:10:56
# @Author  : Kelly Hwong (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os


def k_th(nums: list, k: int):
    '''
    input:
    nums: N 个数
    k: 第 k 个
    output:
    第 k 大的数
    '''
    # 排序法，这样就变成了排序问题
    # 排序法有很多种
    '''
    nums.sort()
    print(nums)
    '''
    # 计数法，用字典
    d = dict()
    for _ in nums:
        if _ not in d:
            d[_] = 1
        else:
            d[_] += 1
    # 得到了每个数有多少个
    max_num = max(d.keys())
    '''
    for _ in reversed(range(max_num+1)):
        if _ in d.keys():
            d[]
    '''
    return nums[k-1]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[:k-1]

def main():
    nums = [10, 30, 5, 7, 12, 20, 3, 3, 10]
    k = 3
    print(k_th(nums, k))


if __name__ == "__main__":
    main()
