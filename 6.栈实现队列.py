from collections import deque


class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, val):
        return self.items.append(val)

    def pop(self):
        return self.items.pop()

    def top(self):  # 返回栈顶值
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0


# %%
class MyQueue:
    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x):
        '''
         Push element x to the back of queue.
        :param x:
        :return:
        type x:int
        rtype:void
        '''
        self.s1.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype:int
        :return:
        """
        if not self.s2.empty():
            return self.s2.pop()
        while not self.s1.empty():
            val = self.s1.pop()
            self.s2.push(val)
        return self.s2.pop()

    def peak(self):
        """
        Get the front element.
        :rtype:int
        :return:
        """
        if not self.s2.empty():
            return self.s2.top()
        while not self.s1.empty():
            val = self.s1.pop()
            self.s2.push(val)
        return self.s2.pop()

    def empty(self):
        """
        Returns whether the queue is empty.
        rtype:bool
        :return:
        """
        return self.s1.empty() and self.s2.empty()


def test():
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.pop())
    print(q.pop())
    print(q.pop())


test()