__author__ = 'fengpeng'


class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        self.dfs(word, "", res, 0, 0)
        return res

    def dfs(self, word, abb, res, count, cur):
        if cur == len(word):
            if count != 0:
                res.append(abb + str(count))
            else:
                res.append(abb)
        else:
            self.dfs(word, abb, res, count + 1, cur + 1)
            self.dfs(word, abb + ("" if count == 0 else str(count)) + word[cur], res, 0, cur + 1)


print Solution().generateAbbreviations("abcd")