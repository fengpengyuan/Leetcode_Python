__author__ = 'fengpeng'


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted(words, key=lambda x: len(x), reverse=True)

        for i in xrange(len(words) - 1):
            mask1 = self.getMask(words[i])
            for j in xrange(i+1, len(words)):
                mask2 = self.getMask(words[j])
                if not (mask1 & mask2):
                    return len(words[i]) * len(words[j])
        return 0


    def getMask(self, word):
        mask = 0
        for c in word:
            mask |= (1 << (ord(c) - ord('a')))
        return mask


words = ["a", "aa", "ab", "abcd", "xy"]

print Solution().maxProduct(words)