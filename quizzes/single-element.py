#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Aug-01-19 12:14
# @Author  : Your Name (you@example.org)
# @Link    : https://leetcode.com/discuss/interview-question/346626/google-phone-screen-single-element

import os


def single_element(nums):
    """
    孤独的元素一定在中间
    """
    # for i, num in enumerate(nums):
    for i in range(0, len(nums)-1-1, 2):
        if nums[i] != nums[i+1]:
            return nums[i]


def main():
    nums = [2, 2, 1, 2, 2]
    nums = [2, 2, 1, 1, 9, 9, 5, 2, 2]
    nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2]
    ret = single_element(nums)
    print(ret)


if __name__ == "__main__":
    main()
