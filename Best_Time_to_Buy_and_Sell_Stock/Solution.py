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
        lowest = prices[0]
        for i in xrange(1, n):
            if prices[i] < lowest:
                lowest = prices[i]
            if prices[i] - lowest > res:
                res = prices[i] - lowest

        return res

    # return the dates
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n = len(prices)
        if n < 2:
            return 0
        max = 0
        lowest = prices[0]
        res = [0, -1]
        lowestIdx = 0
        for i in xrange(1, n):
            if prices[i] <= lowest:
                lowest = prices[i]
                lowestIdx = i
            if prices[i] - lowest > max:
                max = prices[i] - lowest
                res[1] = i
                res[0] = lowestIdx

        return res

prices=[12, 13, 10, 6, 4, 18, 1]
print Solution().maxProfit2(prices)