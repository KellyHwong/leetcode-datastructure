#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Aug-01-19 09:37
# @Author  : Kelly Hwong (you@example.org)
# @Link    : https://www.youtube.com/watch?v=jYQEkkwUBxQ

import os


def poison():
    """
    老鼠和毒药问题
    100个瓶子，99个水，1个毒
    怎么减少老鼠伤亡
    老鼠可以喝好几个瓶子的东西（瓶子里的液体足量）
    这个算法的本质是归并搜索，如何归并的问题
    这里用二进制归并
    """
    number = [_ for _ in range(1, 100+1)]
    """
    1~100在7bit内
    1: 0000 0001
    100: 0110 0100
    7位就够了，7只老鼠瓶子
    喝第7位有1、第i位有1、第1位有1的
    死了的那只，说明第i位有1的有毒
    但是第i位有1的不止一个瓶子
    一直重复到瓶子编号唯一为止
    时间复杂度为O(logN)
    """


def poison2():
    """
    按照上面的安排
    做哪儿一只老鼠更不容易死
    """
    pass


def main():
    poison()


if __name__ == "__main__":
    main()
