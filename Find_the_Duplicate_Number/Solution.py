__author__ = 'fengpeng'


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

    def findDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        beg, end = 0, len(nums) - 1
        while beg <= end:
            m = (beg + end) / 2
            count = 0
            for i in nums:
                if i <= m:
                    count += 1
            if count <= m:
                beg = m + 1
            else:
                end = m - 1
        return beg

    def findDuplicate3(self, nums):
        beg, end = 0, len(nums) - 1

        while beg < end:
            m = (beg + end) / 2
            count = 0
            for num in nums:
                if num <= m:
                    count += 1
            if count <= m:
                beg = m + 1
            else:
                end = m
        return beg


nums = [1, 3, 2, 4, 5, 4]

print Solution().findDuplicate2(nums)