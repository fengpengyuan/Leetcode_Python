__author__ = 'fengpeng'


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i2, i3, i5 = 0, 0, 0
        f2, f3, f5 = 2, 3, 5
        dp = [0] * n
        dp[0] = 1

        for i in xrange(1, n):
            minV = min(f2, f3, f5)
            dp[i] = minV
            if minV == f2:
                i2 += 1
                f2 = 2 * dp[i2]
            if minV == f3:
                i3 += 1
                f3 = 3 * dp[i3]
            if minV == f5:
                i5 += 1
                f5 = 5 * dp[i5]
        return dp[n - 1]

    def nthUglyNumber2(self, n):
        """
        :type n: int
        :rtype: int
        """
        q2, q3, q5 = [1], [1], [1]

        for i in xrange(n):
            minV = min(q2[0], q3[0], q5[0])
            if minV == q2[0]:
                q2.pop(0)
            if minV == q3[0]:
                q3.pop(0)
            if minV == q5[0]:
                q5.pop(0)
            q2.append(minV * 2)
            q3.append(minV * 3)
            q5.append(minV * 5)
        return minV


n = 6
print Solution().nthUglyNumber2(9)