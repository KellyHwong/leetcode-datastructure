class Stack(object):
    """docstring for Stack"""
    def __init__(self, *args):
        super(Stack, self).__init__()
        self.list = []
        if args:
            self.list = args[0]
    def pop(self):
        try:
            return self.list.pop()
        except IndexError as e:
            print("Stack is empty!")
            return None
        else:
            raise
        finally:
            pass
    def push(self, e):
        self.list.append(e)
    def top(self):
        return self.list[-1]
    def get_length(self):
        return len(self.list)

def main():
    # s = Stack([1,2,3])
    l = [1,2,3]
    s = Stack(l)
    '''
    l = [1,2,3]
    for e in l:
        s.push(e)
    '''
    print(s.list)
    print(dir(s))

if __name__ == '__main__':
    main()