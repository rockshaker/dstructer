# -*- coding:utf-8 -*-
# Q:
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法。


class Solution:
    def jumpFloorII(self, number):
        # write code here
        '''
        f(n) = f(n-1)+f(n-2)+f(n-3)+ .. + f(1)+1
        1: 1=1
        2: 2=2
        3: 1+2+1=4
        4: 1+2+1+2+1+1=8
        5: 8+4+2+1+1=16
        '''
        return 2**(number-1)
