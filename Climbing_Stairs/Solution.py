__author__ = 'fengpeng'


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        first, second = 1, 2
        for i in xrange(3, n + 1):
            total = first + second
            first = second
            second = total
        return total