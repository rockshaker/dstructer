#!/usr/bin/python2.7


'''
Question:
    一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''


class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2

        cache = {}
        if number in cache:
            return cache[number]
        else:
            return self.jumpFloor(number-1) + self.jumpFloor(number-2)


class Solution2:
    def jumpFloor(self, number):
        # write code here
        if number == 1 or number == 2:
            return number

        a = 1
        b = 2
        c = 3

        for i in range(3, number+1):
            c = a + b
            a = b
            b = c
        return c
