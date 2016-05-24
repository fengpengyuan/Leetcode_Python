__author__ = 'fengpeng'


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res, sol = [], []
        self.dfs(s, sol, res)
        return res

    def dfs(self, s, sol, res):
        if not s:
            res.append(list(sol))
        for i in xrange(len(s)):
            s1 = s[: i + 1]
            print s1
            if self.isPalindrome(s1):
                sol.append(s1)
                self.dfs(s[i+1:], sol, res)
                sol.pop()

    def isPalindrome(self, s):
        return s == s[::-1]


print Solution().partition("aab")

s = "abcd"
print s[:2]