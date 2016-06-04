import collections
import sys

__author__ = 'fengpeng'


class WordDistance(object):
    def __init__(self, words):
        self.dict = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.dict[word].append(i)

    def shortest(self, word1, word2):
        l1 = self.dict[word1]
        l2 = self.dict[word2]

        idx1, idx2, res = 0, 0, sys.maxint
        while idx1 < len(l1) and idx2 < len(l2):
            res = min(res, abs(l1[idx1] - l2[idx2]))
            if l1[idx1] < l2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
        return res


words = ["practice", "makes", "perfect", "coding", "makes"]
wd = WordDistance(words)

print wd.shortest("makes", "coding")

