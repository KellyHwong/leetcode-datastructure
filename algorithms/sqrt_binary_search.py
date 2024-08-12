#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-31-19 16:55
# @Author  : Kan HUANG (dianhuangkan@gmail.com)
# @Link    : https://leetcode.com/explore/learn/card/binary-search/125/template-i/950/

import os


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        if x == 0:
            return 0
        left, right = 1, x - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid*mid <= x and x < (mid+1)*(mid+1):
                return mid
            elif mid*mid < x:
                left = mid + 1
            elif mid*mid >= x:
                right = mid - 1
        return -1


def main():
    sol = Solution()
    ret = sol.mySqrt(8)
    ret = sol.mySqrt(9)
    print(ret)


if __name__ == "__main__":
    main()
