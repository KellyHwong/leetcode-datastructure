#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-08-19 21:41
# @Author  : Kan HUANG (dianhuangkan@gmail.com)
# @Link    : https://leetcode.com/problems/subsets/discuss/329218/Python-DP

import os
import collections


def subset_dp(nums: list) -> list:
    dp = collections.defaultdict(list)
    dp[1] = [[i] for i in nums]

    for x in range(2, len(nums)+1):
        for up in dp[x-1]:
            for i in range(nums.index(up[-1])+1, len(nums)):
                dp[x].append(up + [nums[i]])

    ans = [[]]
    for val in dp.values():
        for v in val:
            ans.append(v)
    return ans


class Solution:
    def subsets(self, nums: list) -> list:
        return subset_dp(nums)


def main():
    nums = [1, 2, 3, 4]
    ans = subset_dp(nums)
    print(ans)


if __name__ == "__main__":
    main()
