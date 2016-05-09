__author__ = 'fengpeng'


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        while i <= j:
            mid = (i + j) / 2
            if not isBadVersion(mid):
                i = mid + 1
            else:
                j = mid - 1
        return i


def isBadVersion(version):
    pass