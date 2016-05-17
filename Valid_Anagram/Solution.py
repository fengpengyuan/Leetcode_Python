import collections

__author__ = 'fengpeng'


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        d1, d2 = collections.defaultdict(int), collections.defaultdict(int)

        for c in s:
            d1[c] += 1
        for c in t:
            d2[c] += 1
        for i in d1:
            if d1[i] != d2[i]:
                return False
        return True

    def isAnagram3(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return collections.Counter(s).items() == collections.Counter(t).items()


print Solution().isAnagram3('a', 'a')