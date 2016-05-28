__author__ = 'fengpeng'


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in xrange(len(s)):
            res = res * 26 + (ord(s[i]) - ord('A')) % 26 + 1
        return res


print Solution().titleToNumber("AD")