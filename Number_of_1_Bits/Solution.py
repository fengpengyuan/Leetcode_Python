__author__ = 'fengpeng'


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in xrange(32):
            if n & 1:
                count += 1
            n >>= 1
        return count

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count


print Solution().hammingWeight(11)