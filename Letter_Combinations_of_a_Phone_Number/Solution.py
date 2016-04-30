__author__ = 'fengpeng'


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        res = []
        dic = {0: "", 1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wzyx"}
        self.dfs(digits, dic, "", res, 0)
        return res

    def dfs(self, digits, dic, sol, res, cur):
        if cur == len(digits):
            res.append(sol)
            return
        s = dic[int(digits[cur])]
        for i in range(len(s)):
            self.dfs(digits, dic, sol + s[i], res, cur + 1)

    def letterCombinations2(self, digits):
        if not digits:
            return []
        dic = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wzyx"]
        res = ['']
        for digit in digits:
            tem = []
            for d in dic[int(digit)]:
                for cur in res:
                    tem.append(cur + d)
            res = tem
        return res


print(Solution().letterCombinations2("345"))
