#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-29 23:27:34
# @Update  : Oct-03-20 00:59
# @Author  : Kan HUANG (dianhuangkan@gmail.com)
# @RefLink : https://docs.python.org/zh-cn/3/library/collections.html?highlight=deque#collections.deque

import os
from collections import deque


def list_test():
    """Python built-in list
    """
    l = []
    l.append(9)
    l.append(9)
    l.append(6)
    print(l)


def deque_test():
    """Python built-in deque
    """
    d = deque("ghi")
    ret = d.pop()
    ret = d.popleft()


def main():
    list_test()


if __name__ == "__main__":
    main()
