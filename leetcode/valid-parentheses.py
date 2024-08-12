#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-23-19 10:18
# @Author  : Kan HUANG (dianhuangkan@gmail.com)
# @Link    : http://example.org

import os


class Solution:
    def isValid(self, s: str) -> bool:
        def matched(c1, c2):
            if c1 == '(' and c2 == ')':
                return True
            if c1 == '[' and c2 == ']':
                return True
            if c1 == '{' and c2 == '}':
                return True
            return False
        stack = []
        for c in s:
            # 开放符号
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            # 封闭符号
            elif c == ')' or c == ']' or c == '}':
                if stack == []:
                    return False
                if matched(stack[-1], c):
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        return False


class Solution2:
    def isValid(self, s: str) -> bool:
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


"""
用字典加速配对
https://leetcode.com/problems/valid-parentheses/discuss/339064/python-32ms-stack-set-dict
"""


class Solution3:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        if len(s) % 2:
            return False
        stack = []
        open_brackets = {'(', '[', '{'}
        closed_brackets = {')', ']', '}'}
        open_to_closed = {'(': ')', '[': ']', '{': '}'}

        for i in range(len(s)):
            if s[i] in open_brackets:
                stack.append(s[i])
            elif s[i] in closed_brackets:
                if not stack or (stack and open_to_closed[stack.pop()] != s[i]):
                    return False
        return stack == []


def test1():
    sol = Solution3()
    # Input: "()[]{}"
    # Output: true
    s = "()[]{}"
    s = "(])"
    print(s)
    ret = sol.isValid(s)
    print(ret)


if __name__ == "__main__":
    test1()
