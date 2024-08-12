#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-24 20:13:16
# @Author  : Kan HUANG (dianhuangkan@gmail.com)
# @Link    : https://zh.wikipedia.org/zh-cn/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F
# @Version : $Id$

import os
import random


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:  # 等于的时候归并到左边，确保排序是稳定的
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result


def merge_sort(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = l[:mid]
    right = l[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


if __name__ == "__main__":
    '''
    l = []
    for _ in range(20):
        l.append(random.randint(0, 100))
    print(l)
    '''
    l = [82, 77, 39, 68, 32, 48, 39, 81, 37, 59,
         61, 10, 19, 13, 44, 78, 67, 61, 65, 50]
    print("original:", l)
    print("Sorted:", merge_sort(l))
