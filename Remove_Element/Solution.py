__author__ = 'fengpeng'


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = 0
        for i in xrange(len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1
        return l

nums=[1,2,1,2]

print Solution().removeElement(nums, 1)