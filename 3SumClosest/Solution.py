import sys

__author__ = 'fengpeng'


class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = sys.maxint
        for i in range(len(nums) - 2):
            beg, end = i + 1, len(nums) - 1
            while beg < end:
                s = nums[i] + nums[beg] + nums[end]
                if s == target:
                    return s
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    beg += 1
                else:
                    end -= 1
        return res





