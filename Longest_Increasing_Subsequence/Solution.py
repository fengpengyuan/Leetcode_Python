__author__ = 'fengpeng'


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp) if dp else 0


arr = [10, 9, 2, 5, 3, 7, 101, 18]
print Solution().lengthOfLIS(arr)