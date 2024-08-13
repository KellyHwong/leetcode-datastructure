#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024/08/13 14:48:59
# @Author  : Kelley HUANG (dianhuangkan@gmail.com)
# @Link    : https://leetcode.com/problems/invert-binary-tree/

# 递归、BFS、DFS，3种遍历方式实现翻转
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTreeBFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """invertTreeBFS
        层序遍历方式翻转
        """
        # 用队列实现
        if root == None:
            return root
        queue = []
        queue.append(root)
        while not len(queue) == 0:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)

        return root


class Solution:
    def invertTreeDFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """深度优先遍历的方式翻转
        """
        # 用栈实现
        if root == None:
            return root
        queue = []
        queue.append(root)
        while not len(queue) == 0:
            node = queue.pop()
            node.left, node.right = node.right, node.left
            # 先进后出，则left子节点先被访问
            if node.right != None:
                queue.append(node.right)
            if node.left != None:
                queue.append(node.left)

        return root
