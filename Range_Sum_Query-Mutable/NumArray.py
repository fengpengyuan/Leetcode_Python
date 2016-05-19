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
        self.arr = [nums[0]]
        for i in xrange(1, len(nums)):
            self.arr.append(self.arr[-1] + nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        for k in xrange(i, len(self.arr)):
            self.arr[k] += val-self.nums[i]
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.arr[j]-self.arr[i]+self.nums[i]



# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5]
numArray = NumArray(nums)
print numArray.sumRange(0, 1)
print numArray.update(1, 10)
print numArray.sumRange(1, 2)