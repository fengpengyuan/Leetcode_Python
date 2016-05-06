__author__ = 'fengpeng'


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        map = {}
        start = 0
        res = 0
        windonwStart = 0
        for i in xrange(len(s)):
            if s[i] in map:
                map[s[i]] += 1
                res = max(res, i - start + 1)
                if res == i - start + 1:
                    windonwStart = start
            elif len(map) < k:
                map[s[i]] = 1
                res = max(res, i - start + 1)
                if res == i - start + 1:
                    windonwStart = start
            else:
                while len(map) == k:
                    if map[s[start]] == 1:
                        del map[s[start]]
                    else:
                        map[s[start]] -= 1
                    start += 1
                map[s[i]] = 1

        print s[windonwStart:windonwStart + res]
        return res

    def lengthOfLongestSubstringKDistinct2(self, s, k):
        j, numDic, res, map = 0, 0, 0, {}
        for i in xrange(len(s)):
            while j < len(s):
                if s[j] in map:
                    map[s[j]] += 1
                    res = max(res, j - i + 1)
                    j += 1
                elif numDic < k:
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


s = "ecebaabcd"

print Solution().lengthOfLongestSubstringKDistinct(s, 3)
print Solution().lengthOfLongestSubstringKDistinct2(s, 3)