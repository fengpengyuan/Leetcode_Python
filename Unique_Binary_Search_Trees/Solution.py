__author__ = 'fengpeng'


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        res = 0
        for i in xrange(1, n + 1):
            left = self.numTrees(i - 1)
            right = self.numTrees(n - i)
            res += left * right
        return res

    def numTrees1(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in xrange(2, n + 1):
            for j in xrange(i):
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[n]


print Solution().numTrees(3)
print Solution().numTrees1(3)