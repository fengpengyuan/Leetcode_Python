__author__ = 'fengpeng'


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        self.dfs(digits, "", res, 0)
        return res

    def dfs(self, digits, sol, res, cur):
        if cur == len(digits):
            res.append(str(sol))
            return
        s = self.getString(digits[cur] - '0')
        for i in range(len(s)):
            self.dfs(digits, sol + s[i], res, cur + 1)


    def getString(self, i):
        dic = {0: "", 1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wzyx"}
        return dic[i]


print(Solution().letterCombinations("123"))
