__author__ = 'fengpeng'


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)):
            while nums[i] != i + 1:
                if nums[i] <= 0 or nums[i] > len(nums) or nums[i] == nums[nums[i] - 1]:
                    break
                nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
        for i in xrange(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

    def firstMissingPositive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, n = 0, len(nums)

        while i < n:
            print nums[i]
            if 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] # danger! to be safe, do it like java or c++
            else:
                i += 1

        for i in xrange(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


nums = [2,1]
print Solution().firstMissingPositive2(nums)