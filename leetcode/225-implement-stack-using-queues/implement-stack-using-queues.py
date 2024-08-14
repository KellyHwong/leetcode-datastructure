#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024/08/14 13:59:33
# @Author  : Kelley HUANG (dianhuangkan@gmail.com)
# @Ref     : https://leetcode.com/problems/implement-stack-using-queues/description/

from typing import List


class MyStack:

    def __init__(self):
        # a queue is a python list that supports pop(0)
        self.queue1 = []  # queue1 stores current elements
        self.queue2 = []  # queue2 receive new element

    def transport(self, queue1: List[int], queue2: List[int]):
        """transport elements in queue1 to queue2 by FIFO
        """
        while not len(queue1) == 0:
            queue2.append(queue1.pop(0))

    def push(self, x: int) -> None:
        self.queue2.append(x)
        self.transport(self.queue1, self.queue2)
        self.transport(self.queue2, self.queue1)

    def pop(self) -> int:
        if not len(self.queue1) == 0:
            return self.queue1.pop(0)
        else:
            return None

    def top(self) -> int:
        if not len(self.queue1) == 0:
            return self.queue1[0]
        else:
            return None

    def empty(self) -> bool:
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


def main():
    my_stack = MyStack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.pop()
    my_stack.peek()


if __name__ == '__main__':
    main()
