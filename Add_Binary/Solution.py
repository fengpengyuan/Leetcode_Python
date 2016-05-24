__author__ = 'fengpeng'


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a or not b:
            return a if not b else b
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        res = ''
        while i >= 0 or j >= 0:
            s = carry
            if i >= 0:
                s += int(a[i])
            if j >= 0:
                s += int(a[i])
            res = "".join((str(s % 2), res))
            carry = s / 2
            i, j = i - 1, j - 1

        if carry == 1:
            return '1' + res
        return res


print Solution().addBinary("11", "1")
