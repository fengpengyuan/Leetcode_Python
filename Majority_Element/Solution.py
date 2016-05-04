__author__ = 'fengpeng'


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, count = nums[0], 1

        for i in xrange(1, len(nums)):
            if nums[i] == res:
                count += 1
            else:
                count -= 1
                if count == 0:
                    res, count = nums[i], 1
        return res
