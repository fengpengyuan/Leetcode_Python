__author__ = 'fengpeng'


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n1, n2 = len(s), len(t)
        dp = [[0 for i in xrange(n2+1)] for _ in xrange(n1 + 1)]

        for i in xrange(n1 + 1):
            dp[i][0] = 1

        for i in xrange(1, n1 + 1):
            for j in xrange(1, n2 + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n1][n2]


S = "rabbbit"
T = "rabbit"

print Solution().numDistinct(S, T)

dp1=[[0]*3]*3
print dp1
dp1[0][0]=1
print dp1