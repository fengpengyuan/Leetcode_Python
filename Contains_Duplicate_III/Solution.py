__author__ = 'fengpeng'


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        dict = {}
        for i, num in enumerate(nums):
            for x in xrange(t):
                if num - x in dict:
                    if i - dict[num - x] <= k:
                        return True
            dict[num] = i
        return False

    ########################################################
    # solution 2  bucket sort
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False
        dict = {}
        w = t + 1
        for i in xrange(len(nums)):
            m = nums[i] / w
            if m in dict:
                return True
            if m - 1 in dict and abs(nums[i] - dict[m - 1]) < w:
                return True
            if m + 1 in dict and abs(nums[i] - dict[m + 1]) < w:
                return True
            dict[m] = nums[i]

            if i >= k:
                del dict[nums[i - k] / w]
        return False

