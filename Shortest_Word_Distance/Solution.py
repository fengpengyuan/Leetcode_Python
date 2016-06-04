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
        res = sys.maxint
        for i, word in enumerate(words):
            if word == word1:
                idx1 = i
            if word == word2:
                idx2 = i
            if idx1 != -1 and idx2 != -1:
                res = min(res, abs(idx1 - idx2))
        return res

words = ["practice", "makes", "perfect", "coding", "makes"]
print Solution().shortestDistance(words, "coding", "practice")

