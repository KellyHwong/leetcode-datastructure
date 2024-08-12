#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jun-14-21 17:07
# @Author  : Kan HUANG (dianhuangkan@gmail.com)
# @RefLink : https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """三指针法翻转单链表
        """
        if not head:
            return None
        p, q = head, head.next
        head.next = None
        while q:
            r = q.next
            q.next = p
            p = q
            q = r
        head = p

        return head


def main():
    pass


if __name__ == "__main__":
    main()
