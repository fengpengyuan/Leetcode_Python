__author__ = 'fengpeng'


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4 or len(s) > 12:
            return []
        res, sol = [], ""
        self.dfs(s, sol, res, 0)
        return res

    def dfs(self, s, sol, res, dep):
        if dep == 3 and self.isValidNum(s):
            res.append(sol + "." + s)
        for i in xrange(1, 4):
            if i < len(s):
                num = s[0: i]
                if self.isValidNum(num):
                    self.dfs(s[i:], sol + ("" if not sol else ".") + num, res, dep + 1)

    def isValidNum(self, s):
        if s[0] == '0':
            return len(s) == 1
        num = int(s)
        return 1 <= num <= 255


print Solution().restoreIpAddresses("1111")