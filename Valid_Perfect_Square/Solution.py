from math import sqrt
import math

__author__ = 'fengpeng'


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        dp = [i for i in xrange(num + 1)]

        for i in xrange(1, num + 1):
            for j in xrange(int(math.sqrt(i)+1)):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        print dp
        return dp[num] == 1


    def isPerfectSquare2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 0, num
        while left<=right:
            mid=(left+right)/2
            if mid*mid==num:
                return True
            elif mid*mid>num:
                right = mid-1
            else:
                left=mid+1
        return False


print Solution().isPerfectSquare(16)

print Solution().isPerfectSquare2(16)