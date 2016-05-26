import collections

__author__ = 'fengpeng'


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        map = {}
        start = 0
        res = 0
        for i in xrange(len(s)):
            if s[i] in map:
                map[s[i]] += 1
                res = max(res, i - start + 1)
            else:
                if len(map) < 2:
                    map[s[i]] = 1
                else:
                    while len(map) == 2:
                        map[s[start]] -= 1
                        if map[s[start]] == 0:
                            del map[s[start]]
                        start += 1
                    map[s[i]] = 1
        return res

    def lengthOfLongestSubstringTwoDistinct2(self, s):
        j, numDic, res, map = 0, 0, 0, {}
        for i in xrange(len(s)):
            while j < len(s):
                if s[j] in map:
                    map[s[j]] += 1
                    res = max(res, j - i + 1)
                    j += 1
                elif numDic < 2:
                    map[s[j]] = 1
                    numDic += 1
                    res = max(res, i - j + 1)
                    j += 1
                else:
                    break
            if s[i] in map:
                map[s[i]] -= 1
                if map[s[i]] == 0:
                    del map[s[i]]
                    numDic -= 1
        return res

    def lengthOfLongestSubstringTwoDistinct3(self, s):
        map = collections.defaultdict(int)
        count, start, res = 0, 0, 0
        for i, c in enumerate(s):
            map[c] += 1
            if map[c] == 1:
                count += 1
            while count > 2:
                map[s[start]] -= 1
                if map[s[start]] == 0:
                    count -= 1
                start += 1
            res = max(res, i - start + 1)
        return res


s = "ecedc"

print Solution().lengthOfLongestSubstringTwoDistinct(s)
print Solution().lengthOfLongestSubstringTwoDistinct2(s)
print Solution().lengthOfLongestSubstringTwoDistinct3(s)