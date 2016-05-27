import sys

__author__ = 'fengpeng'


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        globalMax, preLocalMax, preLocalMin = nums[0], nums[0], nums[0]
        for i in xrange(1, len(nums)):
            localMax = max(nums[i], preLocalMax * nums[i], preLocalMin * nums[i])
            localMin = min(nums[i], preLocalMax * nums[i], preLocalMin * nums[i])
            globalMax = max(localMax, globalMax)

            preLocalMin = localMin
            preLocalMax = localMax
        return globalMax


nums = [-2, -3, -1]

print Solution().maxProduct(nums)
