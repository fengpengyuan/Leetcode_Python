__author__ = 'fengpeng'


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ""
        res = ''
        while n > 0:
            n -= 1
            res = chr(n % 26 + ord('A')) + res
            n /= 26
        return res

    def convertToTitle2(self, n):
        """
        :type n: int
        :rtype: str
        """
        return "" if n == 0 else self.convertToTitle((n - 1) / 26) + chr((n - 1) % 26 + ord('A'))


print Solution().convertToTitle(26)

print Solution().convertToTitle2(26)