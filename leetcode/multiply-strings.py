#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-18 19:55:42
# @Author  : Kelly Hwong (you@example.org)
# @Link    : https://leetcode.com/problems/multiply-strings/
# @Version : $Id$

import os

# 其实就是字符串相乘
# 中间要不要转字符串
# 没必要
# 九九乘法表，查表法

# 字符串相乘，要解决Python字符串相乘的问题
# 中间过程为整数，结果为字符串
# 拆解字符串
# 按位相乘
# 进位
# 第一种，竖式乘法式

# 第二种，乘好连加式（一个一个加）

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = int(num1)
        num2 = int(num2)
        return num1 * num2

def gen99Table():
    d = dict()
    for i in range(10):
        for j in range(10):
            d[(str(i), str(j))] = str(i * j)
    print(d)

def main():
    # gen99Table()
    s = Solution()
    print(s.multiply("123", "456"))

if __name__ == '__main__':
    main()
