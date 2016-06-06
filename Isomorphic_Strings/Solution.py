__author__ = 'fengpeng'


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        d1, d2 = {}, {}
        for i in xrange(len(s)):
            if s[i] in d1 and d1[s[i]] != t[i]:
                return False
            else:
                d1[s[i]] = t[i]
            if t[i] in d2 and d2[t[i]] != s[i]:
                return False
            else:
                d2[t[i]] = s[i]
        return True

print Solution().isIsomorphic("foo", "bar")