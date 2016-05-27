__author__ = 'fengpeng'


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        n = len(nums)
        if n == 0:
            return res
        left, right = [0] * n, [0] * n
        left[0], right[n - 1] = 1, 1

        for i in xrange(1, n):
            left[i] = nums[i - 1] * left[i - 1]
        for i in xrange(n - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]

        for i in xrange(n):
            res.append(left[i] * right[i])
        return res

    def productExceptSelf2(self, nums):
        n = len(nums)
        res = [0] * n
        res[0] = 1

        for i in xrange(1, n):
            res[i] = nums[i - 1] * res[i - 1]
        right = 1
        for i in xrange(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res


nums = [1, 2, 3, 4, 5, 6]
print Solution().productExceptSelf2(nums)