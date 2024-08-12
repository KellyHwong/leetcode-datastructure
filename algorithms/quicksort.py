#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-21 05:39:55
# @Author  : Kan HUANG (dianhuangkan@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

import os
import resource
import sys
import random
import time

RECUR = 0
# 一种递归写法
# 一种原地写法
'''
function quicksort(q)
{
    var list less, pivotList, greater
    if length(q) ≤ 1
    return q
    else
    {
        select a pivot value pivot from q
        for each x in q except the pivot element
        {
            if x < pivot then add x to less
            if x ≥ pivot then add x to greater
        }
        add pivot to pivotList
        return concatenate(quicksort(less), pivotList, quicksort(greater))
    }
}
'''


def quicksort_one_turn(q: list):
    smaller, larger = [], []
    pivot = q[0]
    for _ in q:
        if _ < pivot:
            smaller.append(_)
        elif _ >= pivot:
            larger.append(_)
    return smaller, larger


def quicksort(q: list):
    if len(q) <= 1:
        return q
    smaller, larger = [], []
    pivot = q.pop(0)  # 要去掉弹出来的
    for _ in q:
        if _ < pivot:
            smaller.append(_)
        elif _ >= pivot:
            larger.append(_)
    return quicksort(smaller) + [pivot] + quicksort(larger)


def main():
    # print(resource.getrlimit(resource.RLIMIT_STACK))  # (67104768, 67104768) bytes
    # print(sys.getrecursionlimit()) # 1000

    N = 1000000
    l = [random.randint(-2**31, 2**31-1) for _ in range(N)]
    # print(l)
    start = time.clock()
    q = quicksort(l)
    elapsed = (time.clock() - start)
    # print(q)
    print("Time used:", elapsed)


if __name__ == "__main__":
    main()
