#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Dec-31-19 01:25
# @Author  : Kelley HUANG (dianhuangkan@gmail.com)
# @RefLink : https://leetcode.com/problems/powx-n/
# @RefLink : 快速幂算法 https://baike.baidu.com/item/%E5%BF%AB%E9%80%9F%E5%B9%82/5500243


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 快速幂算法
        if (n == 0):
            return 1
        if (n % 2 == 0):
            _ = self.myPow(x, n/2)
            return _*_
        if (n < 0):
            return 1 / self.myPow(x, -n)

        return x * self.myPow(x, n-1)


def main():
    sol = Solution()
    test = {'x': 2, 'n': 10}
    res = sol.myPow(**test)
    print(res)


if __name__ == "__main__":
    main()
