import collections

__author__ = 'fengpeng'


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = collections.defaultdict(int)

        for c in s:
            d[c] += 1
        odd = 0
        for k in d:
            if d[k] % 2 == 1:
                odd += 1
        return odd < 2