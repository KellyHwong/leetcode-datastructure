#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Aug-01-19 08:56
# @Author  : Your Name (you@example.org)
# @Link    : https://leetcode.com/problems/search-insert-position/

import os


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        if nums[left] >= target:
            return left
        if nums[right] < target:
            return right + 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return left


def test1():
    """
    nums is sorted
    Input: [1,3,5,6], 5
    Output: 2
    """
    sol = Solution()
    nums = [1, 3, 5, 6]
    target = 5  # 2
    nums = [1, 3, 5, 6]
    target = 2  # 1
    nums = [1, 3, 5, 6]
    target = 0  # 0
    nums = [1, 3, 5, 6]
    target = 7
    ret = sol.searchInsert(nums, target)
    print(ret)


def main():
    test1()


if __name__ == "__main__":
    main()
