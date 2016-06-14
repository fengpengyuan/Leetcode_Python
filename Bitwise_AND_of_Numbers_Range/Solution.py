__author__ = 'fengpeng'


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        move = 0
        while m != n:
            m, n = m >> 1, n >> 1
            move += 1
        return m << move

print Solution().rangeBitwiseAnd(5, 7)