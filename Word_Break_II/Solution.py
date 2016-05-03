__author__ = 'fengpeng'


class Solution(object):
    # def wordBreak(self, s, wordDict):
    #     """
    #     :type s: str
    #     :type wordDict: Set[str]
    #     :rtype: List[str]
    #     """
    #     res, sol = [], ""
    #     self.dfs(s, wordDict, sol, res)
    #     return res
    #
    # # def dfs(self, s, wordDict, sol, res):
    # # if s in wordDict:
    # #         res.append(sol+s)
    # #         return
    # #     for i in xrange(1, len(s)):
    # #         word = s[:i]
    # #         if word in wordDict:
    # #             self.dfs(s[i:], wordDict, sol + word + ' ', res)
    #
    # def dfs(self, s, wordDict, sol, res):
    #     if not s:
    #         res.append(sol.strip())
    #         return
    #     for i in xrange(1, len(s) + 1):  # differ from above
    #         word = s[:i]
    #         if word in wordDict:
    #             self.dfs(s[i:], wordDict, sol + word + ' ', res)


    # Solution2################################
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        dict = {}
        return self.dfs(s, wordDict, dict)

    def dfs(self, s, wordDict, dict):
        if s in dict:
            return dict[s]
        res = []
        for i in xrange(1, len(s)+1):
            w = s[:i]
            rem = s[i:]
            if w in wordDict:
                temp = self.dfs(rem, wordDict, dict)
                for words in temp:
                    res.append(w + " " + words)
                if not rem:
                    res.append(w)
        dict[s] = res
        return res


s = "catsanddog"
dict = set(["cat", "cats", "and", "sand", "dog"])

print Solution().wordBreak(s, dict)