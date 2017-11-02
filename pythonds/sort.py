class Sort:
    def bubble_sort1(self, nums):
        n = len(nums)

        for i in range(n):
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

    def bubble_sort2(self, nums):
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

    def quick_sort(self, nums):
        pass

if __name__ == "__main__":
    s = Sort()
    print s.bubble_sort1([1, 3, 2, 7, 9, 8])
    print s.bubble_sort2([5, 2, 6, 8, 1, 10])
