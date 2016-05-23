__author__ = 'fengpeng'


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        if m == 0:
            return 0
        n = len(dungeon[0])
        dp = [[0] * n for _ in xrange(m)]

        dp[m - 1][n - 1] = max(0 - dungeon[m - 1][n - 1], 0)

        for i in xrange(m - 2, -1, -1):
            dp[i][n - 1] = max(0, dp[i + 1][n - 1] - dungeon[i][n - 1])
        for i in xrange(n - 2, -1, -1):
            dp[m - 1][i] = max(0, dp[m - 1][i + 1] - dungeon[m - 1][i])

        for i in xrange(m - 2, -1, -1):
            for j in xrange(n - 2, -1, -1):
                dp[i][j] = max(0, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
        return dp[0][0] + 1

