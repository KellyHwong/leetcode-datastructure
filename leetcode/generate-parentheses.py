#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-23-19 10:42
# @Author  : Kan HUANG (dianhuangkan@gmail.com)
# @Link    : https://leetcode.com/problems/generate-parentheses/

import os


"""
暴力法
"""
from itertools import combinations


def isValid(s: str) -> bool:
    # stack init
    stk = list()
    for c in s:
        # ignore 1st character
        if len(stk) != 0:
            # if it is correct pair
            if (stk[-1] == "(" and c == ")") \
                    or (stk[-1] == "[" and c == "]") \
                    or (stk[-1] == "{" and c == "}"):
                # then pop and continue
                stk.pop()
                continue
        stk.append(c)
    return not len(stk)


class Solution:
    def generateParenthesis(self, n: int) -> list:
        # ((( C_6^3
        # 插入)))
        valid = []
        comb = list(combinations(list(range(2*n)), n))
        for case in comb:
            s = [')'] * 2*n
            for _ in case:
                s[_] = '('
            s = ''.join(s)
            if isValid(s):
                valid.append(s)
        return valid


def main():
    sol = Solution()
    n = 3
    ret = sol.generateParenthesis(n)
    print(ret)


if __name__ == "__main__":
    main()
