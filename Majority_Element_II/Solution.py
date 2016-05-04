import sys

__author__ = 'fengpeng'


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # if len(nums) < 3:
        #     return list(set(nums))
        first, second = sys.maxint, sys.maxint
        count1, count2 = 0, 0

        for num in nums:
            if num == first:
                count1 += 1
            elif num == second:
                count2 += 1
            elif count1 == 0:
                first = num
                count1 = 1
            elif count2 == 0:
                second = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1, count2 = 0, 0
        for num in nums:
            if num == first:
                count1 += 1
            elif num == second:
                count2 += 1

        res = []
        if count1 > len(nums) / 3:
            res.append(first)
        if count2 > len(nums) / 3:
            res.append(second)

        return res

print "ff"
print Solution().majorityElement([1, 2]), "ss"