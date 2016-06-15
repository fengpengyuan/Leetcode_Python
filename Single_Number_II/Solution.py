__author__ = 'fengpeng'


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in xrange(32):
            t = 1 << i
            sum = 0
            for num in nums:
                if (t & num) != 0:
                    sum += 1
            if sum % 3 != 0:
                res |= t
        return res

    # the above works in Java, but not in python, for negative numbers
    # python will convert it to long.

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        neg = 0
        for i in xrange(32):
            t = 1 << i
            sum = 0
            for num in nums:
                if num < 0:
                    neg += 1
                    num = ~(num - 1)
                if (t & num) != 0:
                    sum += 1
            if sum % 3 != 0:
                res |= t
        if neg % 3 != 0:
            return -res
        return res


nums = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]

print Solution().singleNumber2(nums)