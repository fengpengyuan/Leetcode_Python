__author__ = 'fengpeng'


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        n = len(nums)
        t = n*(n+1)/2

        return t-s

nums=[0, 1, 3]
print Solution().missingNumber(nums)