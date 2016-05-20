__author__ = 'fengpeng'


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        n = len(nums)
        self.n = n
        self.sumArr = [0] * (n + 1)
        self.nums = nums
        for i in xrange(n):
            self.add(i + 1, nums[i])

    def add(self, i, val):
        while i <= self.n:
            self.sumArr[i] += val
            i += self.lowbit(i)

    def lowbit(self, x):
        return x & (-x)

    def sum(self, x):
        res = 0
        while x > 0:
            res += self.sumArr[x]
            x -= self.lowbit(x)
        return res


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        # x = val - self.nums[i]
        # i += 1
        # while i <= self.n:
        # self.sumArr[i] += x
        #     i += self.lowbit(i)
        self.add(i + 1, val - self.nums[i])
        self.nums[i] = val


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.nums:
            return 0
        return self.sum(j + 1) - self.sum(i)


# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 4]
numArray = NumArray(nums)
print numArray.sumRange(0, 1)
print numArray.update(1, 0)
print numArray.sumRange(1, 2)