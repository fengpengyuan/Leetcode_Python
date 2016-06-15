__author__ = 'fengpeng'


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)
        t = 1
        for i in xrange(1, num + 1):
            if i == t:
                res[i] = 1
                t *= 2
            else:
                res[i] = 1 + res[i - t / 2]
        return res

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)

        for i in xrange(1, num + 1):
            res[i] = res[i / 2]
            if i % 2 == 1:
                res[i] += 1
        return res


print Solution().countBits(5)