import sys

__author__ = 'fengpeng'


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        dp = [0] * n
        dp[0] = 1
        indices = [0] * len(primes)

        for i in xrange(1, n):
            dp[i] = sys.maxint
            for j in xrange(len(primes)):
                dp[i] = min(dp[i], primes[j] * dp[indices[j]])
            for j in xrange(len(primes)):
                if dp[i] % primes[j] == 0:
                    indices[j] += 1
        print dp
        return dp[n - 1]

primes=[2, 7, 13, 19]

Solution().nthSuperUglyNumber(12, primes)
