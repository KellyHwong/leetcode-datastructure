#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-22-19 11:27
# @Author  : Kan HUANG (dianhuangkan@gmail.com)
# @Link    : http://example.org

import os
import time


def shift_left():
    start = time.clock()
    N = 10000000  # 一千万次
    for _ in range(N):
        i = 1
        # i *= 31  # 0.587474s
        # i *= 32  # 0.588701s
        i <<= 5  # 0.890978s
    elapsed = (time.clock() - start)
    print("Time used:", elapsed)


def shift_right():
    start = time.clock()
    N = 10000000  # 一千万次
    for _ in range(N):
        i = 10000
        # i /= 31  # 0.5884s
        # i /= 32  # 0.59352s
        i >>= 5  # 0.824442s
    elapsed = (time.clock() - start)
    print("Time used:", elapsed)


if __name__ == "__main__":
    shift_right()
