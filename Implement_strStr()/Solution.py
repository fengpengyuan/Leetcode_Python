__author__ = 'fengpeng'


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle):
            return -1

        for i in xrange(len(haystack) - len(needle) + 1):
            j = 0
            while j < len(needle):
                if haystack[j + i] != needle[j]:
                    break
                j += 1
            if j == len(needle):
                return i
        return -1