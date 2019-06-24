class SLinkedList:
    """
    单链表
    本身即指针
    既是节点，也是指针，Python风格
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def traverse(self):
        ptr = self
        # print(ptr.data)
        while ptr:
            # print(ptr.data)
            yield ptr.data
            ptr = ptr.next

    # 一种是非遍历的
    def reverse(self):
        ptr = self
        while ptr:
            ptr = ptr.next
            ptr.next.next = ptr

    def recursiveReverse(self):
        pass


if __name__ == "__main__":

    n1 = SLinkedList("Mon")
    n2 = SLinkedList("Tue")
    n3 = SLinkedList("Wed")
    n4 = SLinkedList("Thur")
    n5 = SLinkedList("Fri")
    n6 = SLinkedList("Sat")
    n7 = SLinkedList("Sun")

    # linking
    n6.next = n7
    n5.next = n6
    n4.next = n5
    n3.next = n4
    n2.next = n3
    n1.next = n2

    '''
    print(e2.next)
    # 结果为e3内存地址<__main__.Node object at 0x0000001A0F9644BE0>
    print(e2.next.data)
    # 结果为e3所代表的值Wed
    '''

    n1.traverse()
    # 翻转链表 TODO
