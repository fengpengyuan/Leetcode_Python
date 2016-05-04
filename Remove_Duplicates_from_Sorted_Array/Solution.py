__author__ = 'fengpeng'


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        j = 1
        for i in xrange(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j


nums = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3]

print Solution().removeDuplicates(nums)
