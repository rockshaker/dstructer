# -*- coding:utf-8 -*-
class Solution:
    """
    我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
    """
    def rectCover(self, number):
        # write code here
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2

        n1 = 2
        n2 = 1
        while number > 2:
            n1 = n1 + n2
            n2 = n1 - n2
            number -= 1

        return n1
