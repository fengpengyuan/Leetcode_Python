__author__ = 'fengpeng'


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        beg, end = 0, x
        while beg <= end:
            m = (beg + end) / 2
            if m * m == x:
                return m
            if m * m > x:
                end = m - 1
            else:
                beg = m + 1
        return end

    # newton method
    def mySqrt2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        last, cur = 1, x
        while cur != last:
            last = cur
            cur = (cur + x / cur) / 2.0
        return int(cur)


print Solution().mySqrt(8)
print Solution().mySqrt2(8)