__author__ = 'fengpeng'


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(n, 0, 0, "", res)
        return res

    def dfs(self, n, left, right, sol, res):
        if left == n and left == right:
            res.append(sol)
        if left < n:
            self.dfs(n, left + 1, right, sol + "(", res)
        if right < left:
            self.dfs(n, left, right + 1, sol + ")", res)


    def generateParenthesis2(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [""]
        for i in xrange(n):
            t = []
            for p in res:
                pos = p.rfind('(')
                for j in xrange(pos + 1, len(p) + 1):
                    s = "".join(p[:j]) + '(' + "".join(p[j:]) + ')'
                    t.append(s)
            res = t
        return res

    def generateParenthesis3(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return ['']
        res = []
        for i in xrange(n):
            left = self.generateParenthesis3(i)
            right = self.generateParenthesis3(n - i - 1)
            for p1 in left:
                for p2 in right:
                    res.append('(' + p1 + ')' + p2)
        return res

    def generateParenthesisdp(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [['']] * (n + 1)

        for i in xrange(1, n + 1):
            t = []
            for j in xrange(i):
                inside = dp[j]
                tail = dp[i - j - 1]

                for p1 in inside:
                    for p2 in tail:
                        t.append("(" + p1 + ")" + p2)
            dp[i] = t
        return dp[n]


print Solution().generateParenthesis(3)
print Solution().generateParenthesis3(1)
print Solution().generateParenthesisdp(2)