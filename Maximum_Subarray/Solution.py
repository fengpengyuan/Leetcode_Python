__author__ = 'fengpeng'


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, m = 0, 0
        for i in xrange(len(nums)):
            s += nums[i]
            if s < 0:
                s = 0
            if s > m:
                m = s
        if m == 0:
            m = nums[0]
            for num in nums:
                m = max(m, num)
        return m

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        globalMax, localMax = nums[0], nums[0]
        for i in xrange(1, len(nums)):
            localMax = max(localMax+nums[i], nums[i])
            globalMax = max(globalMax, localMax)
        return globalMax


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print Solution().maxSubArray(nums)