__author__ = 'fengpeng'


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
        stk = []
        res = 0
        last = -1
        for i in xrange(len(s)):
            if s[i] == '(':
                stk.append(i)
            else:
                if stk:
                    stk.pop()
                    if stk:
                        res = max(res, i - stk[-1])
                    else:
                        res = max(res, i - last)
                else:
                    last = i
        return res

    def longestValidParentheses2(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0] * n
        res = 0
        for i in xrange(n - 2, -1, -1):
            if s[i] == '(':
                j = i + dp[i + 1] + 1
                if j < n and s[j] == ')':
                    dp[i] = dp[i + 1] + 2
                    if j + 1 < n:
                        dp[i] += dp[j + 1]
                    res = max(res, dp[i])
        return res

    def longestValidParentheses3(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
        stk = []
        res = 0
        for i in xrange(len(s)):
            if s[i] == '(':
                stk.append(i)
            else:
                if not stk:
                    stk.append(i)
                else:
                    if s[stk[-1]] == '(':
                        stk.pop()
                        res = max(res, i - (stk[-1] if stk else -1))
                    else:
                        stk.append(i)
        return res


print Solution().longestValidParentheses2("((()()")

print Solution().longestValidParentheses2(")()(")

print Solution().longestValidParentheses3(")()(")