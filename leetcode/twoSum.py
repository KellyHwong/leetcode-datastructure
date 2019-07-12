#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-12-19 23:01
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import os


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        d = {}
        for i in range(len(nums)):
            toFind = target - nums[i]
            if toFind in d:
                return [d[toFind], i]
            else:
                d[nums[i]] = i


def main():
    s = Solution()

    nums = [2, 7, 11, 15]
    target = 9
    ans = s.twoSum(nums, target)
    print(ans)


if __name__ == "__main__":
    main()
