# -*- coding:utf-8 -*-
#
# 在不借助第三个变量的情况下,把两个 int 的变量 X 、 Y 的值互换,用任何自己熟
# 悉的编程语言完成
#


class Solution:

    @staticmethod
    def solve(x, y):
        x = x + y
        y = x - y
        x = x - y
        return x, y

if __name__ == "__main__":
    print Solution.solve(2, 3)
