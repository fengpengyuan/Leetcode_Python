import sys

__author__ = 'fengpeng'


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1, idx2 = -1, -1
        same = word1==word2
        res = sys.maxint
        for i, word in enumerate(words):
            if word == word1:
                if same:
                    idx1 = idx2
                    idx2 = i
                else:
                    idx1 = i
            elif word == word2:
                idx2 = i
            if idx1 != -1 and idx2 != -1:
                res = min(res, abs(idx1 - idx2))
        return res

words = ["practice", "makes", "perfect", "coding", "makes"]
print Solution().shortestDistance(words, "coding", "practice")

