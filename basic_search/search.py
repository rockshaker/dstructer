#!/usr/bin/python2.7


class Search(object):

    def __init__(self, nums):
        self._nums = sorted(nums)

    def sequential_search(self, find):
        found = False
        l = len(self._nums)
        i = 0

        while i < l and not found:
            if self._nums[i] == find:
                found = True
            else:
                i += 1
        return found

    def binary_search(self, find):
        l = len(self._nums)
        left = 0
        right = l-1
        found = False

        while left < right and not found:
            mid = (left + right) // 2
            if self._nums[mid] == find:
                found = True
            else:
                if self._nums[mid] < find:
                    left = mid + 1
                else:
                    right = mid - 1

        return found


if __name__ == "__main__":
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    s = Search(testlist)
    print s.sequential_search(3)
    print s.binary_search(13)
