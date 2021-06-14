#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-19-20
# @Author  : Kelly Hwong (dianhuangkan@gmail.com)
# @Link    : http://example.org


class Stack(object):
    """Stack implemented with Python list
    """

    def __init__(self, *args):
        super(Stack, self).__init__()
        self.list = []
        if args:
            self.list = args[0]

    def pop(self):
        """Pop operation of the stack
        """
        try:
            return self.list.pop()
        except IndexError as e:
            print("Stack is empty!")
            return None
        else:
            pass
        finally:
            pass

    def push(self, e):
        """Push operation of the stack
        """
        self.list.append(e)

    def top(self):
        """View top element of the stack
        """
        return self.list[-1]

    def __len__(self):
        return len(self.list)


def main():
    l = [1, 2, 3]
    s = Stack(l)  # directly initialized by a list

    # initialized by push operations
    l = [1, 2, 3]
    s = Stack()
    for e in l:
        s.push(e)

    print(s.list)
    for _ in range(len(s)):
        s.pop()
        print(s.list)


if __name__ == '__main__':
    main()
