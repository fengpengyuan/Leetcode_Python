__author__ = 'fengpeng'


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ss = str.split(" ")
        if len(pattern) != len(ss):
            return False
        dict = {}
        for i in range(len(pattern)):
            if pattern[i] in dict and dict.get(pattern[i]) != ss[i]:
                return False
            if pattern[i] not in dict and ss[i] in dict.values():
                return False
            dict[pattern[i]] = ss[i]
        return True

    def wordPattern2(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ss = str.split()
        if len(pattern) != len(ss):
            return False
        dic1, dic2 = {}, {}
        for p, s in zip(pattern, ss):
            if p not in dic1:
                dic1[p] = s
            if s not in dic2:
                dic2[s] = p
            if dic1[p] != s or dic2[s] != p:
                return False
        return True


pattern = "abba"
str = "dog cat cat fish"

print Solution().wordPattern2(pattern, str)
