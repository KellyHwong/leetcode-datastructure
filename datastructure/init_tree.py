#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-16 00:12:24
# @Author  : Kelly Hwong (you@example.org)
# @Link    : https://zh.wikipedia.org/zh-cn/二叉树#存儲二元樹的方法
# @Version : $Id$

from tree import Tree, TreeNode
from stack import Stack
from queue import LinkQueue

def main():
    elements = [1, 2, 3, 4, 0, 5, 6, 0, 7]
    tree_nodes = []

    for e in elements:
        if e == 0:
            tree_nodes.append(None)
        else:
            tree_nodes.append(TreeNode(e))
    # print(tree_nodes)
    node_queue = LinkQueue()
    node_queue.push(tree_nodes[0])
    i = 1
    while i < len(tree_nodes):
        node = node_queue.pop()
        node_queue.push(tree_nodes[i])
        i += 1
        node.lchild = node_queue.rear.data
        node_queue.push(tree_nodes[i])
        i += 1
        node.rchild = node_queue.rear.data

    tree = Tree(tree_nodes[0])
    l = []
    ret = tree.pre_order_iter(tree.root)
    # node_queue.traverse()
    print(ret)

if __name__ == '__main__':
    main()
