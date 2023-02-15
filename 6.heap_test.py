from linked_list import *

from heapq import heapify, heappop
class Solution:
    def mergeKLists(self, lists):
        """
        type lists:List[ListNode]
        rtype:ListNode
        """
        #读取所有节点值
        h = []
        for node in lists:
            while node:
                h.append(node.val)
                node = node.next
        if not h:
            return None
        #构造一个最小堆
        heapify(h)#转换成最小堆

        #构造链表
        root = ListNode(heappop(h))
        curnode = root
        while h:
            nextnode = ListNode(heappop(h))
            curnode.next = nextnode
            curnode = nextnode
        return root
h = Solution()

l1 = [1,2,54,6,7,0]
ListNode_1 = ListNode_handle()
l = list_to_linked(ListNode_1, l1)
ListNode_1.print_ListNode(l)
# h.mergeKLists(l)# 这个有些问题