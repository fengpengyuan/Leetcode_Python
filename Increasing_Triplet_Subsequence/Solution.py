import sys

__author__ = 'fengpeng'


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        s, m = sys.maxint, sys.maxint

        for num in nums:
            if num <= s:
                s = num
            elif num <= m:
                m = num
            else:
                return True
        return False
