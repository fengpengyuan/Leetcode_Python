__author__ = 'fengpeng'


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, left, right):
        if left == right:
            return nums[left]
        if left + 1 == right:
            return min(nums[left], nums[right])
        if nums[left] < nums[right]:
            return nums[left]
        m = (left + right) / 2
        if nums[m] > nums[left]:
            return self.helper(nums, m, right)
        else:
            return self.helper(nums, left, m)

    def findMin2(self, nums):
        i, j = 0, len(nums) - 1
        while i < j:
            m = (i + j) / 2
            if nums[m] < nums[j]:
                j = m
            else:
                i = m + 1
        return nums[i]

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1

        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
            m = (start + end) / 2
            if nums[m] >= nums[start]:
                start = m + 1
            else:
                end = m
        return nums[start]


nums = [3, 4, 5, 1, 2]

print Solution().findMin2(nums)