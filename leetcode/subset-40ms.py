#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-08-19 21:40
# @Author  : Your Name (you@example.org)
# @Link    : https://leetcode.com/problems/subsets/discuss/329658/44-ms-Python-solution

import os


def main():
    pass


if __name__ == "__main__":
    pass


class Solution:
    def subsets(self, nums):
        self.result = []

        curResult = []
        self.solve(nums, curResult)
        return self.result

    def solve(self, nums, curResult):

        if len(nums) == 0:
            self.result.append(curResult)
        else:
            newResult = curResult[:]  # copies the list
            newResult.append(nums[0])

            self.solve(nums[1:], curResult)
            self.solve(nums[1:], newResult)
