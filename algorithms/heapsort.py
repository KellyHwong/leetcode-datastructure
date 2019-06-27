#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-21 15:34:49
# @Author  : Kelly Hwong (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from datastructure.tree import Tree
from utils.logger import logger
import os
import random
import sys


def heapify(l: list, n: int, i):
    # print(l)

    left = 2 * i + 1
    right = 2 * i + 2

    max = i
    if left < n and l[left] > l[max]:
        max = left
    if right < n and l[right] > l[max]:
        max = right
    if max != i:
        # logger.info("exchange {} and {}".format(i, max))
        _ = l[max]
        l[max] = l[i]
        l[i] = _
        # heapify(l, len(l), max)
        heapify(l, n, max)


def build_heap(l: list):
    """
    注意Python参数传的是引用
    """
    last_node = len(l) - 1
    parent = (last_node - 1) // 2
    for i in reversed(range(parent+1)):
        heapify(l, len(l), i)


def heap_sort(l: list):
    """
    注意Python参数传的是引用
    """
    # 建立最大堆
    build_heap(l)
    logger.info("build:{}".format(l))
    for i in reversed(range(len(l))):
        _ = l[i]
        l[i] = l[0]
        l[0] = _
        logger.info(l)
        heapify(l, n=i, i=0)


def main():
    # l = [random.randint(0, 99) for _ in range(10)]
    l = [78, 79, 23, 85, 42, 53, 79, 71, 3, 64]
    # l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    logger.info(l)
    heap_sort(l)
    logger.info(l)
    """
    用真·树构造一个堆
    """
    '''
    # 堆的构造方法就是树的遍历过程的逆过程
    # 左边，右边，下一层，左边，右边
    # 数据结构，队列
    # 构造一个队列，初始头节点
    # 进一个节点，后面加该节点的左右子节点
    tree = Tree(l[0])
    link_queue = LinkQueue()
    for i in range(10):
        link_queue.push(i)
    link_queue.traverse()
    '''
    """
    但是没有必要这样
    用数组就行了
    """


if __name__ == "__main__":
    main()
