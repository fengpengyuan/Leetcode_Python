__author__ = 'fengpeng'


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        res = 0
        for i in xrange(1, n):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res