__author__ = 'fengpeng'


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not s:
            return True
        if s in wordDict:
            return True
        for i in range(1, len(s)):
            word = s[:i]
            print word
            if word in wordDict and self.wordBreak(s[i:], wordDict):
                return True
        return False

    def wordBreak2(self, s, wordDict):
        if not s:
            return True
        dp = [True]
        for i in range(1, len(s)+1):
            dp.append(False)
            for j in range(i):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
                    break
        print dp
        return dp[len(s)]

wordDict = {"leet", "code"}

print Solution().wordBreak2("leetcode", wordDict)
