__author__ = 'fengpeng'


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num
        # get the last set bit
        lowbit = xor & -xor
        res = [0, 0]

        for num in nums:
            if num & lowbit:
                res[0] ^= num
            else:
                res[1] ^= num
        return res