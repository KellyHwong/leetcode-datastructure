#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-23-19 08:39
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import os


def reversePolish(s):
    """
    逆波兰表达式
    """
    s = s.split()
    stk = []
    for ele in s:
        if ele.isdigit():
            stk.append(int(ele))
        elif ele == "+":
            # 弹2压1
            op1 = stk.pop()
            op2 = stk.pop()
            stk.append(op2 + op1)
        elif ele == "-":
            # 弹2压1
            op1 = stk.pop()
            op2 = stk.pop()
            stk.append(op2 - op1)  # 注意先弹出的是被减数
        elif ele == "*":
            # 弹2压1
            op1 = stk.pop()
            op2 = stk.pop()
            stk.append(op2 * op1)
    return stk[0]


def infix2Postfix(s):
    """
    中缀表达式转换成后缀表达式
    """
    priority = {"+": "1", "-": "1", "*": "2", "/": "2"}
    s = s.split()
    stk = []
    out = []
    for ele in s:
        # Operand
        if ele.isdigit():
            out.append(ele)
        # Operation
        elif ele in priority.keys():
            if stk == []:
                stk.append(ele)
            # 相同或者优先
            if priority[ele] >= priority[stk[-1]]:
                out.append(ele)
            else:
                out.append(stk.pop())
                out.append(ele)
        # Open parenthese
        elif ele == '(':
            stk.append(ele)
        # Close parenthese
        elif ele == ')':
            while cur = stk.pop() != '(':

    pass


def main():
    s = "5 1 2 + 4 * + 3 -"
    ret = reversePolish(s)
    # print(ret)
    s = "1 + 2 * 3 + ( 4 * 5 + 6 ) * 7"
    ret = infix2Postfix(s)


if __name__ == "__main__":
    main()
