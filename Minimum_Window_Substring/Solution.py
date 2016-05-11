__author__ = 'fengpeng'


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict = {}
        for c in t:
            if c not in dict:
                dict[c] = 0
            dict[c] += 1
        start, total = 0, 0
        windowStart, minLen = 0, len(s) + 1
        found = {}
        for i, c in enumerate(s):
            if c not in dict:
                continue
            if c not in found:
                found[c] = 0
            found[c] += 1
            if found[c] <= dict[c]:
                total += 1
            if total == len(t):
                while s[start] not in dict or found[s[start]] > dict[s[start]]:
                    if s[start] in dict and found[s[start]] > dict[s[start]]:
                        found[s[start]] -= 1
                    start += 1
                if i - start + 1 < minLen:
                    minLen = i - start + 1
                    windowStart = start

        if minLen > len(s):
            return ""
        return s[windowStart: windowStart + minLen]

S = "ADOBECODEBANC"
T = "ABC"
print Solution().minWindow(S,T)