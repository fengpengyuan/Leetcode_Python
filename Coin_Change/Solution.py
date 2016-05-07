import sys

__author__ = 'fengpeng'


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [amount + 1] * amount

        for i in xrange(1, amount + 1):
            for j in xrange(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        return -1 if dp[amount] > amount else dp[-1]


    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] * (amount + 1)

        for i in xrange(1, amount + 1):
            t = sys.maxint
            for coin in coins:
                if i >= coin and dp[i - coin] != -1:
                    t = min(t, dp[i - coin] + 1)
            dp[i] = -1 if t == sys.maxint else t
        return dp[-1]

    # got LTE if use coins[j] instead of "coin in coins", weird


coins = [370, 417, 408, 156, 143, 434, 168, 83, 177, 280, 117]
print Solution().coinChange(coins, 9953)