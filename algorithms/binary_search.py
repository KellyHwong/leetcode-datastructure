#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-31-19 15:30
# @Author  : Kan HUANG (dianhuangkan@gmail.com)
# @Link    : http://example.org

import os
import random

random.per


class Solution:
    def search(self, nums: list, target: int) -> int:
        left, right = 0, len(nums) - 1
        mid = left
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1


def binary_search1():
    """
    Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4
    """
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    nums = [-1, 0, 3, 5, 9, 12]
    target = 2

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1


def binary_search(arr, left, right, hkey):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == hkey:
            return mid
        elif arr[mid] < hkey:
            left = mid + 1
        elif arr[mid] > hkey:
            right = mid - 1
    return -1


def binary_search_iter(arr, start, end, hkey):
    if start > end:
        return -1
    mid = start + (end - start) / 2
    if arr[mid] > hkey:
        return binary_search(arr, start, mid - 1, hkey)
    if arr[mid] < hkey:
        return binary_search(arr, mid + 1, end, hkey)
    return mid


def main():
    ret = binary_search1()
    print(ret)


if __name__ == "__main__":
    main()
