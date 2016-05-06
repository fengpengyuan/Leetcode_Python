__author__ = 'fengpeng'


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in xrange(1, len(s)):
            cur, pre = s[i], s[i - 1]
            if dict[cur] > dict[pre]:
                res -= dict[pre]
            else:
                res += dict[pre]
        res += dict[s[-1]]
        return res

    def romanToInt(self, s):
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in xrange(len(s)):
            res += self.sign(i, s, dict) * dict[s[i]]
        return res

    def sign(self, i, s, dict):
        if i == len(s) - 1:
            return 1
        if dict[s[i]] < dict[s[i + 1]]:
            return -1
        return 1


print Solution().romanToInt('MMXL')



