__author__ = 'fengpeng'


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2147483647
        sign = 1
        if dividend * divisor < 0:
            sign = -1
        dividend, divisor = abs(dividend), abs(divisor)

        res = 0
        while dividend >= divisor:
            shift, t = 0, dividend
            while t >= (divisor << shift):
                shift += 1
            t -= divisor << (shift - 1)
            res += 1 << (shift - 1)
            dividend = t

        res *= sign
        return res if res < INT_MAX else INT_MAX


print Solution().divide(-1, -1)