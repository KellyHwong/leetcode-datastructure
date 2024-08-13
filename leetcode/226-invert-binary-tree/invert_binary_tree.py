#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024/08/13 14:26:53
# @Author  : Kelley HUANG (dianhuangkan@gmail.com)
# @Link    : https://leetcode.com/problems/invert-binary-tree/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 递归实现
        # 翻转一棵树，即互换左右，最后对它的左子树、右子树进行翻转
        if root == None:
            return root
        root.left, root.right = root.right, root.left
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root


def main():
    sol = Solution()


if __name__ == '__main__':
    main()
