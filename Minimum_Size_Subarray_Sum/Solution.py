__author__ = 'fengpeng'


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sum, start = 0, 0
        res = len(nums) + 1
        for i in xrange(len(nums)):
            sum += nums[i]
            while sum >= s:
                res = min(res, i - start + 1)
                sum -= nums[start]
                start += 1

        return 0 if res > len(nums) else res


nums = [2, 3, 1, 2, 4, 3]

print Solution().minSubArrayLen(7, nums)
