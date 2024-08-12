#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-24-19 12:55
# @Author  : Kan HUANG (dianhuangkan@gmail.com)
# @Link    : https://leetcode.com/contest/weekly-contest-80/problems/most-common-word/

import os
import string


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list) -> str:
        """
        Input: 
        paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        banned = ["hit"]
        Output: "ball"
        """
        # translator = str.maketrans('', '', string.punctuation)
        translator = str.maketrans("!?',;.", 6*' ')
        words = paragraph.translate(translator)
        words = words.lower()
        words = words.split()

        d = {}
        for word in words:
            if word not in d.keys():
                d[word] = 1
            else:
                d[word] += 1

        count = 0
        for word in d.keys():
            if word in banned:
                continue
            cur_count = d[word]
            if cur_count > count:  # >= ?
                count = cur_count
                out = word
        return out


def main():
    sol = Solution()
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    paragraph = "a, a, a, a, b,b,b,c, c"
    banned = ["a"]

    ret = sol.mostCommonWord(paragraph, banned)
    print(ret)


if __name__ == "__main__":
    main()
