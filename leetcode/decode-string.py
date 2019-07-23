#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-23-19 08:27
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import os


class Solution:
    def decodeString(self, s: str) -> str:
        """
        表达式问题，逆波兰表达式
        只要把中缀表示法转换为后缀表示法
        中缀表达式是有括号的
        后缀不需要，方面使用栈进行计算
        或者简化为递归
        """
        stack = []
        substring = ""
        for i, c in enumerate(s):
            if c.isdigit():
                weight = int(c)
                stack.append(weight)
            elif c == '[':
                # 表达式开始
                pass
            elif c == ']':
                # 表达式结束，并求值
                pass


def test1():
    sol = Solution()
    # s = "3[a]2[bc]", return "aaabcbc".
    # s = "3[a2[c]]", return "accaccacc".
    s = "3[a]2[bc]"
    ret = sol.decodeString(s)


if __name__ == "__main__":
    test1()
