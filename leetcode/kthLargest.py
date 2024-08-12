#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-08-19 21:10
# @Author  : Kan HUANG (dianhuangkan@gmail.com)
# @Link    : http://example.org

import os
import random


class Solution1:
    def findKthLargest(self, nums: list, k: int) -> int:
        nums.sort()
        return nums[-k]


def quicksort_one_turn(q: list):
    smaller, larger = [], []
    pivot = q[0]
    for _ in q[1:]:
        if _ < pivot:
            smaller.append(_)
        elif _ >= pivot:
            larger.append(_)
    return smaller, larger


"""
Python迭代的劣势在于
每次返回数列都要拷贝
"""


class Solution2:
    def findKthLargest(self, nums: list, k: int) -> int:
        """
        左右法，快速排序的partition思想
        O（N *logK）
        """
        smaller, larger = quicksort_one_turn(nums)
        if len(larger) + 1 < k:
            return self.findKthLargest(smaller, k-len(larger)-1)
        elif len(larger) + 1 == k:
            return nums[0]
        else:
            return self.findKthLargest(larger, k)


class Solution3:
    def findKthLargest(self, nums: list, k: int) -> int:
        """
        左右法，快速排序的partition思想
        类C的原地版本
        TODO
        """
        smaller, larger = quicksort_one_turn(nums)
        if len(larger) + 1 < k:
            return self.findKthLargest(smaller, k-len(larger)-1)
        elif len(larger) + 1 == k:
            return nums[0]
        else:
            return self.findKthLargest(larger, k)


def main():
    s = Solution2()
    nums = [3, 2, 1, 5, 6, 4]
    k = 3
    # N = 20
    # l = [random.randint(0, 100) for _ in range(N)]
    # nums = [0, 43, 43, 87, 20, 44, 43, 9, 23, 97,
    # 6, 59, 95, 9, 49, 3, 12, 96, 23, 32]
    ans = s.findKthLargest(nums, k)
    print(ans)


if __name__ == "__main__":
    main()
