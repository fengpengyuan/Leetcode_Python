__author__ = 'fengpeng'


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial = 1
        nums = []
        for i in xrange(1, n + 1):
            factorial *= i
            nums.append(i)
        res = ''
        k -= 1
        for i in xrange(n):
            factorial /= (n - i)
            index = k / factorial
            res += str(nums[index])
            nums.remove(nums[index])
            k %= factorial
        return res


print Solution().getPermutation(3, 2)