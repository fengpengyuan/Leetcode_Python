__author__ = 'fengpeng'


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in xrange(m + 1)]
        dp[0][0] = True
        for i in xrange(2, n + 1, 2):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if s[i - 1] != p[j - 2] and p[j-2]!='.':
                        dp[i][j] = dp[i][j - 2]
                    elif s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or dp[i - 1][j]
        return dp[m][n]

print Solution().isMatch("aa", "a*")
