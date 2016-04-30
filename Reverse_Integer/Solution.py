import sys

__author__ = 'fengpeng'


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        overflow = False
        if x < 0:
            x = -x
            neg = True
        rev = 0

        while x > 0:
            digit = x % 10
            if (sys.maxint - digit) / 10 > rev:
                rev = rev * 10 + digit
            else:
                overflow = True
                break
            x /= 10
        if overflow:
            return sys.minint if neg else sys.maxint
        else:
            return -rev if neg else rev


    def reverse2(self, x):
        sign = -1 if x < 0 else 1
        x = -x if sign == -1 else x
        res = 0

        while x > 0:
            res = res * 10 + x % 10
            x /= 10
        if res > 2 ** 31 - 1 or res < -2 ** 31 + 1:
            return 0
        return res if sign == 1 else -res


print(Solution().reverse(-123))
