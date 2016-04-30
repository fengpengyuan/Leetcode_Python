__author__ = 'fengpeng'


class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        res = ""
        for i in range(n):
            s1 = self.expandFromCenter(s, i, i)
            s2 = self.expandFromCenter(s, i, i + 1)
            if max(len(s1), len(s2)) > len(res):
                res = s1 if len(s1) > len(s2) else s2
        return res

    def expandFromCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]


s = "abcd"
print(s[0:2])
print(Solution().longestPalindrome("abccb"))