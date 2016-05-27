import sys

__author__ = 'fengpeng'


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # profit1 means sell on day i
        # profit2 means do nothing, rest
        # nice explaination: https://leetcode.com/discuss/73617/7-line-java-only-consider-sell-and-cooldown
        n = len(prices)
        profit1, profit2 = 0, 0
        for i in xrange(1, n):
            t = profit1
            profit1 = max(profit1 + prices[i] - prices[i - 1], profit2)
            profit2 = max(t, profit2)
        return max(profit1, profit2)

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        buy, sell, rest = [0] * n, [0] * n, [0] * n

        buy[0] = -prices[0]
        sell[0] = -sys.maxint

        for i in xrange(1, n):
            rest[i] = max(rest[i-1], sell[i-1])
            buy[i] = max(rest[i-1]-prices[i], buy[i-1])
            sell[i] = buy[i-1]+prices[i]
        return max(rest[n-1], sell[n-1])