#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024/08/13 16:12:27
# @Author  : Kelley HUANG (dianhuangkan@gmail.com)
# @Ref     : https://leetcode.com/problems/implement-queue-using-stacks/description/


class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def in2out(self):
        while not len(self.inStack) == 0:
            self.outStack.append(self.inStack.pop())

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        if len(self.outStack) == 0:
            self.in2out()

        if len(self.outStack) != 0:
            ret = self.outStack.pop()
        else:
            ret = None

        return ret

    def peek(self) -> int:
        if len(self.outStack) == 0:
            self.in2out()

        if len(self.outStack) != 0:
            ret = self.outStack[-1]
        else:
            ret = None

        return ret

    def empty(self) -> bool:
        return len(self.inStack) == 0 and len(self.outStack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


def main():
    my_queue = MyQueue()
    my_queue.push(1)
    my_queue.push(2)
    my_queue.pop()
    my_queue.peek()


if __name__ == '__main__':
    main()
