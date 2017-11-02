# -*- coding:utf-8 -*-
from pythonds.list import UnorderedList


class ReverseList:
    # Q: Reverse a linked list
    def solve(self, head):
        if head is None:
            return None

        prev = None
        current = head

        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev


class MiddleNode:
    # Q: Find the middle node of a linked list
    def solve(self, head):
        p1 = head
        p2 = head
        size = 0
        while p1 is not None:
            size += 1
            p1 = p1.get_next()

        step = size/2
        while step > 0:
            p2 = p2.get_next()
            step -= 1

        return p2


class BackkNode:
    """
    Q:
        输入一个单向链表，输出该链表中倒数第k个节点，链表的倒数第0个节点为链表的尾指针。
    """
    def resolve(self, head, k):
        p1 = head
        p2 = head

        while k > 0:
            p2 = p2.get_next()
            k -= 1

        while p2 is not None:
            p1 = p1.get_next()
            p2 = p2.get_next()
        return p1


if __name__ == "__main__":
    ul = UnorderedList()
    items = [1, 3, 2, 6, 5, 9]
    for item in items:
        ul.add(item)
    ul.list_print()

    rs = ReverseList()
    reversed_list_head = rs.solve(ul.head)
    print reversed_list_head.get_data()
    print reversed_list_head.get_next().get_data()

    bkn = BackkNode()
    print bkn.resolve(ul.head, 2).get_data()
