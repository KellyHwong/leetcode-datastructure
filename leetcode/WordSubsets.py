#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-8-19 22:30
# @Author  : Kelly Hwong
# @Link    : http://example.org


def isIn(str1, str2):
    for c in str1:
        if c in str2:
            pass
        else:
            return False
    return True


"""
Input: A = ["amazon", "apple", "facebook", "google", "leetcode"], B = ["e", "o"]
Output: ["facebook", "google", "leetcode"]
"""
"""
A 是一个集合的集合
B 是一个集合
A中某个集合包含B中所有元素（包括重复），则该集合是B超集（就是子集的定义嘛）
求A中所有这样的集合
关键是判断超集，注意考虑重复，subset2是考虑重复的子集问题，可以做一下

Note: B也是集合的集合，每个元素长度不一定就是1（一个字母）
"""

"""
统计法
"""


str1 = ["e", "o"]
str2 = "facebook"
b = ["a", "p"]
A = ["apple"]

A = ["amazon", "apple", "facebook", "google", "leetcode"]
b = ["e", "o"]

# print(letter_count(b))
# print(letter_count(a))
# print(isSubsetOf(b, a))


def letter_count(word: list):
    d = {}
    for l in word:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1
    return d


def isSubsetOf(b: list, a: list) -> bool:
    db = letter_count(b)
    da = letter_count(a)
    for l in db.keys():
        if l not in da.keys() or db[l] > da[l]:
            return False
    return True


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ans = []
        for a in A:
            a_ = list(a)
            if isSubsetOf(B, a_):
                ans.append(a)
        return ans
