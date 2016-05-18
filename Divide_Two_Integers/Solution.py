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


    def divide2(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2147483647
        neg = (dividend < 0) ^ (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        res, shift = 0, 31

        while shift >= 0:
            while a >= b << shift:
                a -= b << shift
                res += 1 << shift
            shift -= 1
        if neg:
            res = -res
        if res > INT_MAX:
            return INT_MAX
        return res


print Solution().divide2(-1, -1)