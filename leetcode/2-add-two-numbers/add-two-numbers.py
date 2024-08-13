#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Feb-13-20 20:39
# @Author  : Kan HUANG (dianhuangkan@gmail.com)
# @Link    : https://leetcode.com/problems/add-two-numbers/

from typing import List


class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


def build_linked_list(l: List[int]) -> ListNode:
    head = ListNode(l[0])
    tail = head
    for i, e in enumerate(l):
        if i == 0:
            continue
        tail.next = ListNode(e)
        tail = tail.next
    return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = restore_num(l1)
        num2 = restore_num(l2)
        head = convert_to_linked_list(num1+num2)

        return head


def restore_num(l: ListNode):
    # 小端模式，低位在前
    num, base = 0, 1
    ptr = l
    while True:
        num += ptr.val*base
        base *= 10
        ptr = ptr.next
        if ptr is None:
            break
    return num


def convert_to_linked_list(num: int) -> ListNode:
    # 小端模式，低位在前
    head = ListNode(num % 10)
    num = num // 10
    tail = head
    while True:
        if num == 0:
            break
        tail.next = ListNode(num % 10)
        num = num // 10
        tail = tail.next

    return head


def main():
    """
    给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
    请你将两个数相加，并以相同形式返回一个表示和的链表。
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8

    Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

    如果位数超过十位，就涉及大数运算。
    int 范围：-2147483648 ~ 2147483647 (10位)。
    """

    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    head1 = build_linked_list(l1)  # 实际给的输入数据结构
    head2 = build_linked_list(l2)

    num1 = restore_num(head1)
    num2 = restore_num(head2)

    head = convert_to_linked_list(num1+num2)
    num = restore_num(head)
    print(num)

    sol = Solution()


if __name__ == "__main__":
    main()
