__author__ = 'fengpeng'


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return self.helper(nums, 0, n - 1)

    def helper(self, nums, left, right):
        if left == right:
            return left
        if left == right - 1:
            return left if nums[left] > nums[right] else right
        m = (left + right) / 2
        if nums[m - 1] < nums[m] and nums[m] > nums[m + 1]:
            return m
        elif nums[m] < nums[m + 1]:
            return self.helper(nums, m + 1, right)
        else:
            return self.helper(nums, left, m - 1)


    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return self.helper(nums, 0, n - 1)

    def helper(self, nums, left, right):
        if left == right:
            return left
        else:
            m1 = (left + right) / 2
            m2 = (left + right) / 2 + 1
            if nums[m1] > nums[m2]:
                return self.helper(nums, left, m1)
            else:
                return self.helper(nums, m2, right)

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left, right = 0, n - 1

        while left < right:
            m1 = (left + right) / 2
            m2 = (left + right) / 2 + 1
            if nums[m1] < nums[m2]:
                left = m2
            else:
                right = m1
        return left

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums) - 1

        while i <= j:
            m = (i + j) / 2
            if (m == 0 or nums[m] > nums[m - 1]) and (m == len(nums) - 1 or nums[m] > nums[m + 1]):
                return m
            elif m > 0 and nums[m] < nums[m - 1]:
                j = m - 1
            else:
                i = m + 1
        return i


nums = [1, 2, 3, 1]

print Solution().findPeakElement(nums)
