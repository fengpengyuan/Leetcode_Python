__author__ = 'fengpeng'


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return True
        dp = [False] * n
        dp[n - 1] = True

        gap = 1
        for i in xrange(n - 2, -1, -1):
            if nums[i] >= gap:
                dp[i] = True
                gap = 1
            else:
                gap += 1
        return dp[0]

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        last = n - 1
        for i in xrange(n - 2, -1, -1):
            if nums[i] + i >= last:
                last = i
        return last <= 0
