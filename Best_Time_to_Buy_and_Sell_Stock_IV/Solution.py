__author__ = 'fengpeng'


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if k >= n / 2:
            res = 0
            for i in xrange(1, n):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res

        dp = [[0] * n for _ in xrange(k + 1)]

        for i in xrange(1, k + 1):
            for j in xrange(1, n):
                dp[i][j] = dp[i][j - 1]
                for x in xrange(j):
                    dp[i][j] = max(dp[i][j], dp[i - 1][x] + prices[j] - prices[x])
        return dp[k][n - 1]


    # /**
    # * dp[i, j] represents the max profit up until prices[j] using at most i transactions.
    #  * dp[i, j] = max(dp[i, j-1], prices[j] - prices[jj] + dp[i-1, jj]) { jj in range of [0, j-1] }
    #  *          = max(dp[i, j-1], prices[j] + max(dp[i-1, jj] - prices[jj]))
    #  * dp[0, j] = 0; 0 transactions makes 0 profit
    #  * dp[i, 0] = 0; if there is only one price data point you can't make any transaction.
    #  */
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if k >= n / 2:
            res = 0
            for i in xrange(1, n):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res

        dp = [[0] * n for _ in xrange(k + 1)]

        for i in xrange(1, k + 1):
            localMax = dp[i - 1][0] - prices[0]
            for j in xrange(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + localMax)
                localMax = max(localMax, dp[i - 1][j] - prices[j])
        return dp[k][n - 1]

prices=[3,2,6,5,0,3]
print Solution().maxProfit(2, prices)