import math

__author__ = 'fengpeng'


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in xrange(n+1)]
        for i in xrange(1, n + 1):
            dp[i] = i
            for j in xrange(int(math.sqrt(i) + 1)):
                dp[i] = min(dp[i - j * j] + 1, dp[i])
        print dp
        return dp[n]


print Solution().numSquares(3)
