#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-16 00:12:24
# @Author  : Kelly Hwong (you@example.org)
# @Link    : https://zh.wikipedia.org/zh-cn/二叉树#存儲二元樹的方法
# @Version : $Id$

from datastructure.stack import Stack
import sys
import os


class Tree():
    """节点类
    既是节点，也是节点指针
    """

    def __init__(self, data=None, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

    def pre_order(self, root, visit=print):
        """递归实现先序遍历"""
        if root == None:
            return
        visit(root.data)
        self.pre_order(root.lchild, visit=visit)
        self.pre_order(root.rchild, visit=visit)

    def pre_order_iter(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """递归实现先序遍历"""
        if root == None:
            return
        stack = Stack()
        ret = []
        stack.push(root)

        while stack.get_length() > 0:
            node = stack.pop()
            ret.append(node.data)
            # 因为是先入后出，所以后push lchild
            if node.rchild:
                stack.push(node.rchild)
            if node.lchild:
                stack.push(node.lchild)
        return ret

    def in_order(self, root):
        """递归实现前序遍历"""
        if root == None:
            return
        self.in_order(root.lchild)
        print(root.data)
        self.in_order(root.rchild)

    def post_order(self, root):
        """递归实现后序遍历"""
        if root == None:
            return
        self.post_order(root.lchild)
        self.post_order(root.rchild)
        print(root.data)


def main():
    print(sys.path)


if __name__ == '__main__':
    main()
