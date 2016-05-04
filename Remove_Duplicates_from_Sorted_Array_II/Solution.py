__author__ = 'fengpeng'


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        j, count = 1, 1

        for i in xrange(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
                if count < 3:
                    nums[j] = nums[i]
                    j += 1
            else:
                nums[j] = nums[i]
                count = 1
                j += 1
        return j


    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        j = 2
        for i in xrange(2, len(nums)):
            if nums[i] != nums[j - 1] or nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1

        return j


nums = [1, 2, 2]
print Solution().removeDuplicates2(nums)
