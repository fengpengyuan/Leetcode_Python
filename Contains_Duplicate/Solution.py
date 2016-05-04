__author__ = 'fengpeng'


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False


    # joke solution
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))
