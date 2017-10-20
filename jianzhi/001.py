#!/usr/bin/python2.7

# 在一个二维数组中，
# 每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，
# 判断数组中是否含有该整数。

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        found = False

        for i in range(len(array)):
            if target in array[i]:
                found = True
        return found

    def find(self, target, array):
        found = False
        if not array:
            return False

        nrow = len(array)
        ncol = len(array[0])

        # Set the start point at left corner
        row = nrow - 1
        col = 0
        while 0 <= row < nrow and 0 <= col < ncol and not found:
            if array[row][col] == target:
                found = True
            else:
                if array[row][col] > target:
                    row -= 1
                else:
                    col += 1
        return found
