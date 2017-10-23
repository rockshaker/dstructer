# -*- coding:utf-8 -*-
# Question:
#     输入一个链表，从尾到头打印链表每个节点的值。

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        L = []
        head = listNode
        while head:
            L.insert(0, head.val)
            head = head.next
        return L
