__author__ = 'fengpeng'


class Solution(object):
    # brute force
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        i = len(s)
        while i > 1:
            if self.isPalindrome(s[:i]):
                break
            i -= 1
        return s[i:][::-1] + s

    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True

print Solution().shortestPalindrome("acca")