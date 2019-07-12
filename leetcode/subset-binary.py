#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-12-19 16:37
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import os


def subset_binary(nums):
    """
    子集二进制数
    最小的len(n)*0 都没有元素，空集
    最小的len(n)*1 都有元素，该集合本身
    0~2^n-1
    根据二进制数，取集合中都元素
    """
    n = len(nums)
    ans = []
    for b in range(1 << n):
        subset = []
        i = 0
        while b != 0:
            print("b: %d" % b)
            if b & 0x01:
                # print("i: %d" % i)
                # print("b: %d" % b)
                subset.append(nums[i])
            i += 1
            b >>= 1
        ans.append(subset)
    return ans


class Solution:
    def subsets(self, nums: list) -> list:
        return subset_binary(nums)


def main():
    nums = [1, 2, 3, 4]
    nums = [1, 2, 3]
    ans = subset_binary(nums)
    print(ans)


if __name__ == "__main__":
    main()
