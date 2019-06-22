#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-21 15:34:49
# @Author  : Kelly Hwong (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import random
from utils.logger import logger
from datastructure.tree import Tree


def heapsort(nums: list):
    return


def main():
    # 构造最小堆
    # l = [random.randint(0, 99) for _ in range(10)]
    l = [78, 79, 23, 85, 42, 53, 79, 71, 3, 64]
    logger.info(l)
    l.sort()
    logger.info(l)
    tree = Tree(l[0])

    # 堆的构造方法就是树的遍历过程的逆过程
    # 左边，右边，下一层，左边，右边
    # 数据结构，队列，


if __name__ == "__main__":
    main()
