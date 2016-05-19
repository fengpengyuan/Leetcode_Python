__author__ = 'fengpeng'


class Solution(object):
    # the order changed!
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = 0, n - 1
        while i < j:
            while i < n and nums[i] != 0:
                i += 1
            while j > -1 and nums[j] == 0:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while i < len(nums):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1
        while j < len(nums):
            nums[j] = 0
            j += 1

    def moveZeros(self, nums):
        j = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

