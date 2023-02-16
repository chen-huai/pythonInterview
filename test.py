# # 需安装pytest
# import pytest
# def binary_search(array,target):
#
#     if not array:
#         return -1
#     beg,end = 0,len(array)
#     while beg < end:
#         mid = beg + (end - beg)//2
#         if array[mid]==target:
#             return mid
#         elif array[mid]>target:
#             end = mid
#         else:
#             beg = mid + 1
#     return -1
#
# def test():
#     # 相市相
#     # 如何设计测试用例：(等价类划分)
#     # ~正常值功能测试
#     # 边界值（比如最大最小，最左最右值】
#     # -
#     # 异常值（比如None,空值，非法值】
#     #正常值，包含有和无两种结果
#     assert binary_search([0,1,2,3,4,5],1) ==1
#     assert binary_search([0,1,2,3,4,5],6)==-1
#     assert binary_search([0,1,2,3,4,5],-1)==-1
#     #边界值
#     assert binary_search([0,1,2,3,4,5],0) ==0
#     assert binary_search([0,1,2,3,4,5],5) ==5
#     assert binary_search([],0)==0
#     #异常值
#     assert binary_search([], 1)==-1
# if __name__ == '__main__':
#     pytest.main(['test.py'])


# # 链表
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     def reverseList(self,head):
#         """
#         : type head:ListNode
#         : rtype:ListNode
#         """
#         pre = None
#         cur = head
#         while cur:
#             nextnode = cur.next
#             cur.next = pre
#             pre = cur
#             cur = nextnode
#         print(pre)
#         return pre
# test1 = ListNode(2)
# test1 = ListNode(1)
# # test2 = ListNode(2)
# # print(test1 + test2)
# # head = [1,2,3]
# test = Solution()
# testVal = test.reverseList(test1)
# print(testVal)

# 测试1
# class Node:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class LinkedList:
#     def __init__(self)->None:
#         self.header:Node = None
#     def __getitem__(self,item):
#         temp = self.header
#         i = 0
#         while i < item:
#             if temp.next is None:
#                 raise ValueError('index error')
#             temp = temp.next
#             i+=1
#         return temp
#     def __delitem__(self,key):
#         if key ==0:
#             self.header = self.header.next
#             return
#         temp = self.__getitem__(key-1)
#         temp.next = temp.next.next
#     def append(self,index,node:Node):
#         if not issubclass(type(node),Node):
#             raise ValueError('Not a Node')
#         temp = self.__getitem__(index)
#         node.next = temp.next
#         temp.next = node
#
#     def __add__(self, node):
#         if not issubclass(type(node),Node):
#             raise ValueError('Not a Node')
#         temp = self.header
#         if temp is None:
#             self.header = node
#             return self
#         while True:
#             if temp.next is None:
#                 temp.next = node
#                 return self
#             temp = temp.next
#     @property
#     def length(self):
#         temp = self.header
#         l = 0
#         while temp is not None:
#             temp = temp.next
#             l = l+1
#         return l
#     def __str__(self)->str:
#         s = ''
#         temp = self.header
#         while temp != None:
#             s += str(temp.val)+','
#             temp = temp.next
#         return s
# if __name__ == "__main__":
#         ll = LinkedList()
#         ll + Node('123')+Node(9)+Node(6)+Node(6)+Node(13)
#         print(ll)


# # 测试2
# # 迭代器模式
# from collections import deque
# class Stack:
#     def __init__(self):
#         self._deque = deque()
#     def push(self,val):
#         return self._deque.append(val)
#     def pop(self):
#         return self._deque.pop()
#     def empty(self):
#         return len(self._deque) == 0
#     def __iter__(self):
#         res = []
#         for i in self._deque:
#             res.append(i)
#         for i in reversed(res):
#             yield i
# s = Stack()
# s.push(1)
# s.push(2)
# for i in s:
#     print(i)

# # 测试3
# from functools import wraps
# def cache(func):
#     store = {}
#     @wraps(func)
#     def _(n):
#         # print(n,'a')
#         if n in store:
#             return store[n]
#         else:
#             res = func(n)
#             # print(res,'c')
#             store[n]=res
#             return res
#     return _
# @cache
# def f(n):
#     # print(n,'b')
#     if n <1:
#         return 1
#     # print(f(n -1)+f(n - 2))
#     return f(n-1)
#     # return f(n -1)+f(n - 2)
#
# print(f(23))

import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('localhost', 122))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)