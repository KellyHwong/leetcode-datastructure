#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-21-19 19:01
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import os


def hash1(key: str, tablesize: int) -> int:
    """
    散列一个长度（最多）为8的字符串
    C语言char型的范围是1～127，0是字符串结尾
    求和的结果是8～1016=127*7
    这样不是均匀分配（黑皮书说）
    这是因为ASCII表中，可显示字符只占一部分
    """
    hashval = 0
    # 逐个读取字符的ASCII值
    for k in key:
        hashval += ord(k)
    return hashval % tablesize


def hash2(key: str, tablesize: int) -> int:
    """
    假设：字符串的长度至少为3
    一位有小写字母加空格共27种可能
    按位加权相加，相当于27进制
    “3个字母（忽略空格）有26^3=17576种组合，但是参考足够多词汇的词典发现，（我觉得意思是开头三个字母）3个字母的不同组合数实际只有2851”
    """
    assert(len(key) >= 3)
    return (ord(key[0]) + 27 * ord(key[1]) + 729 * ord(key[2])) % tablesize


def hash3(key: str, tablesize: int) -> int:
    """
    因为是大端模式，所以这么写，大端模式即高有效位在低位，而上面的729*key[2]是小端模式
    大端模式的好处是方便用Horner法则计算
    乘法改成乘以32，这样方便移位运算加速
    """
    hashval = 0
    for k in key:
        hashval += (hashval << 5) + ord(k)
    return hashval


def main():
    key = "12345678"
    tablesize = 10007
    hashval = hash1(key, tablesize)
    print(hashval)
    hashval = hash2(key, tablesize)
    print(hashval)
    hashval = hash3(key, tablesize)
    print(hashval)


if __name__ == "__main__":
    main()
