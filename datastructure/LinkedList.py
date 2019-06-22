class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class SLinkedList:
    def __init__(self):
        self.head = None
    def traverse(self):
        ptr = self.head
        # print(ptr.val)
        while ptr:
            print(ptr.val)
            ptr = ptr.next

    # 一种是非遍历的
    def reverse(self):
        ptr = self.head
        while ptr:
            ptr = ptr.next
            ptr.next.next = ptr

    def recursiveReverse(self):
        pass

li = SLinkedList()
n1 = Node("Mon")
n2 = Node("Tue")
n3 = Node("Wed")
n4 = Node("Thur")
n5 = Node("Fri")
n6 = Node("Sat")
n7 = Node("Sun")

# linking
n6.next = n7
n5.next = n6
n4.next = n5
n3.next = n4
n2.next = n3
n1.next = n2
li.head = n1

'''
print(e2.next)
#结果为e3内存地址<__main__.Node object at 0x0000001A0F9644BE0>
print(e2.next.val)
#结果为e3所代表的值Wed
'''

li.traverse()
# 翻转链表

