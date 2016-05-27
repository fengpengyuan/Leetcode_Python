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
        left, right = [0] * n, [0] * n
        lowest = prices[0]
        for i in xrange(1, n):
            lowest = min(lowest, prices[i])
            left[i] = max(left[i - 1], prices[i] - lowest)
        highest = prices[n - 1]

        for i in xrange(n - 2, -1, -1):
            highest = max(highest, prices[i])
            right[i] = max(right[i + 1], highest - prices[i])
        print left
        print right
        res = 0
        for i in xrange(n):
            res = max(res, left[i] + right[i])
        return res


    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        left = [0] * n
        lowest = prices[0]
        for i in xrange(1, n):
            lowest = min(lowest, prices[i])
            left[i] = max(left[i - 1], prices[i] - lowest)

        highest = prices[n - 1]
        rightMax = 0
        res = 0
        for i in xrange(n - 2, -1, -1):
            highest = max(prices[i], highest)
            rightMax = max(rightMax, highest - prices[i])
            res = max(res, rightMax + left[i])
        return res


prices = [2, 1, 2, 0, 1]
print Solution().maxProfit(prices)
print Solution().maxProfit2(prices)