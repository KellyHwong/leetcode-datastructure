#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-08-19 21:10
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import os


class Solution1:
    def findKthLargest(self, nums: list, k: int) -> int:
        nums.sort()
        return nums[-k]


class Solution2:
    def findKthLargest(self, nums: list, k: int) -> int:
        """
        左右法，快速排序的partition思想
        """
        nums.sort()
        return nums[-k]


def main():
    s = Solution1()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    ans = s.findKthLargest(nums, k)
    print(ans)


if __name__ == "__main__":
    main()
