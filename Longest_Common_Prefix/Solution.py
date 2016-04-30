__author__ = 'fengpeng'


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        t = strs[0]

        for i in range(len(t)):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or t[i] != strs[j][i]:
                    return t[:i]
        return t


strs = ["123", "1234", "124"]
print Solution().longestCommonPrefix(strs)

x = 1
for x in range(1, 3):
    print x,
print x