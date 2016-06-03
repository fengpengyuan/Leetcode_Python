__author__ = 'fengpeng'


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==1:
            return nums[0]
        return max(self.helper(nums, 0, n-2), self.helper(nums, 1, n-1))

    def helper(self, nums, l, r):
        preRob, preNotRob = 0, 0
        for i in xrange(l, r+1):
            curRob = preNotRob + nums[i]
            curNotRob = max(preNotRob, preRob)
            preNotRob = curNotRob
            preRob = curRob
        return max(preNotRob, preRob)

nums=[1,2,3,1,4]
print Solution().rob(nums)