__author__ = 'fengpeng'


class Solution(object):
    def numDecodings1(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        self.dfs(s, 0, "", res)
        print res
        return len(res)

    def dfs(self, s, cur, sol, res):
        if cur == len(s):
            res.append(sol)
        for i in xrange(cur, len(s)):
            num = s[cur:i + 1]
            if self.isValidNum(num):
                self.dfs(s, i + 1, sol + chr((int(num) - 1 + ord('A'))), res)

    def isValidNum(self, s):
        if s[0] == '0':
            return False
        return 1 <= int(s) <= 26

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        dp = [1] + [0] * n
        dp[1] = 1 if s[0] != '0' else 0
        for i in xrange(2, n + 1):
            first = int(s[i - 1:i])
            second = int(s[i - 2:i])
            if 1 <= first <= 9:
                dp[i] += dp[i - 1]
            if 10 <= second <= 26:
                dp[i] += dp[i - 2]
        return dp[n]


print Solution().numDecodings1("12")