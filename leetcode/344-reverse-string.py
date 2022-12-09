#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Dec-09-22 11:45
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)
# @RefLink : https://leetcode.com/problems/reverse-string/

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # swap
        # s[0], s[-1]
        # s[i], s[-1-i]
        for i in range(len(s)//2):
            tmp = s[i]
            s[i] = s[-1-i]
            s[-1-i] = tmp

        return None


def main():
    sol = Solution()
    s = "123456"
    s = list(s)

    ans = sol.reverseString(s)
    print(ans)
    print(s)


if __name__ == "__main__":
    main()
