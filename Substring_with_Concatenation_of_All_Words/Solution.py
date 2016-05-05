__author__ = 'fengpeng'


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(words)
        m = len(words[0])
        if s < m * n:
            return []
        res, map = [], {}
        for word in words:
            if word in map:
                map[word] += 1
            else:
                map[word] = 1

        for i in xrange(len(s) - m * n+1):
            j = 0
            found = {}
            while j < len(words):
                sub = s[i + j * m:i + j * m + m]
                if sub not in map:
                    break
                if sub not in found:
                    found[sub] = 1
                else:
                    found[sub] += 1
                if found[sub] > map[sub]:
                    break
                j += 1
            if j == len(words):
                res.append(i)
        return res


s = "barfoothefoobarman"
words = ["foo", "bar"]

print Solution().findSubstring(s, words)

