import math

__author__ = 'fengpeng'


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in xrange(n + 1)]
        for i in xrange(1, n + 1):
            dp[i] = i
            for j in xrange(int(math.sqrt(i) + 1)):
                dp[i] = min(dp[i - j * j] + 1, dp[i])
        print dp
        return dp[n]

    #####################################
    # solution 2
    def numSquares2(self, n):
        level = 0
        q1, q2 = [0], []
        visited = [False] * (n + 1)
        while q1:
            level += 1
            while q1:
                v = q1.pop(0)
                i = 0
                while True:
                    i += 1
                    t = v + i * i
                    if t == n:
                        return level
                    if t > n:
                        break
                    if visited[t]:
                        continue
                    visited[t] = True
                    q2.append(t)
            q1 = q2
            q2 = []
        return 0


print Solution().numSquares(6)
print Solution().numSquares2(20)

