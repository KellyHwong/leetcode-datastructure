#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-12-19 23:01
# @Author  : Kelley HUANG (dianhuangkan@gmail.com)
# @Link    : https://leetcode.com/problems/two-sum

import os


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        d = {}
        for i, num in enumerate(nums):
            to_find = target - num
            _ = d.get(to_find, None)  # 查找表
            if _ is not None:
                return [d[to_find], i]
            else:
                d[num] = i


def main():
    s = Solution()

    nums = [2, 7, 11, 15]
    target = 9
    ans = s.twoSum(nums, target)
    print(ans)  # [0, 1]


if __name__ == "__main__":
    main()
