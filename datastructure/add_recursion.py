#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-18 16:02:11
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

current_sum = 0
def sum_tail(current_sum, n):
    if n == 0:
        return current_sum
    else:
        return sum_tail(current_sum+n, n - 1)

def main():
    n = 6
    current_sum = 0
    s = sum_tail(current_sum, n)
    print(s)

if __name__ == '__main__':
    main()