# -*- coding:utf-8 -*-
# Q:
# Reverse a linked list
from pythonds.list import UnorderedList


class ReverseList:
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
