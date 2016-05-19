__author__ = 'fengpeng'


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if not nums:
            return
        self.nums = nums
        # self.s = []
        # cur = 0
        # for num in nums:
        #     cur += num
        #     self.s.append(cur)
        self.s = [0]
        for num in nums:
            self.s.append(self.s[-1]+num)


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        # return self.s[j] - self.s[i] + self.nums[i]
        return self.s[j+1] - self.s[i]