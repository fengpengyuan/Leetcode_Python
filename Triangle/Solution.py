__author__ = 'fengpeng'


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        if m == 0:
            return 0
        n = len(triangle[m - 1])

        dp = [[0] * n for _ in xrange(m)]

        dp[0][0] = triangle[0][0]
        for i in xrange(1, m):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]

        for i in xrange(1, m):
            for j in xrange(1, len(triangle[i])):
                if j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        return min(dp[m - 1])

    def minimumTotal2(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        if m == 0:
            return 0
        n = len(triangle[m - 1])
        dp = [0] * n
        dp[0] = triangle[0][0]

        for i in xrange(1, m):
            for j in xrange(i, -1, -1):
                if j == 0:
                    dp[j] += triangle[i][j]
                elif j == i:
                    dp[j] = dp[j - 1] + triangle[i][j]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + triangle[i][j]
        return min(dp)


    def minimumTotal3(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        dp = triangle[m - 1]

        for i in xrange(m - 2, -1, -1):
            for j in xrange(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]


triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

print Solution().minimumTotal(triangle)
print Solution().minimumTotal2(triangle)
print Solution().minimumTotal3(triangle)